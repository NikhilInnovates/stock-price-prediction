import torch
import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

MODEL_PATH = "transformer_stock_model.pth"
SCALER_PATH = "scaler.save"

class TransformerModel(torch.nn.Module):
    def __init__(self, input_dim=1, model_dim=64, num_heads=4, num_layers=2, output_dim=1):
        super(TransformerModel, self).__init__()
        self.embedding = torch.nn.Linear(input_dim, model_dim)
        self.transformer = torch.nn.Transformer(
            d_model=model_dim,
            nhead=num_heads,
            num_encoder_layers=num_layers,
            num_decoder_layers=num_layers,
            dim_feedforward=2048,
            dropout=0.1,
            batch_first=True
        )
        self.fc = torch.nn.Linear(model_dim, output_dim)

    def forward(self, src):
        src = self.embedding(src)
        output = self.transformer(src, src)
        output = self.fc(output[:, -1, :])
        return output

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = TransformerModel(input_dim=1, model_dim=64, num_heads=4, num_layers=2, output_dim=1)
model.load_state_dict(torch.load(MODEL_PATH, map_location=device, weights_only=True))
model.to(device)
model.eval()

try:
    scaler = joblib.load(SCALER_PATH)
    print(f"Scaler loaded: {scaler}")
except Exception as e:
    print(f"Error loading scaler: {e}")
    scaler = None

class PredictionInput(BaseModel):
    data: list[float]

@app.post("/predict")
async def predict(input_data: PredictionInput):
    if scaler is None:
        return {"error": "Scaler not loaded"}
    try:
        print(f"Received data: {input_data.data}")
        input_array = np.array(input_data.data).reshape(-1, 1)
        print(f"Input array shape: {input_array.shape}")
        scaled_input = scaler.transform(input_array)
        print(f"Scaled input: {scaled_input}")
        tensor_input = torch.tensor(scaled_input, dtype=torch.float32).to(device).unsqueeze(0)
        print(f"Tensor input shape: {tensor_input.shape}")
        with torch.no_grad():
            pred = model(tensor_input)
            print(f"Prediction shape: {pred.shape}, Prediction: {pred}")
            pred_value = pred[0, 0].item()
        unscaled_pred = scaler.inverse_transform([[pred_value]])[0][0]
        print(f"Unscaled prediction: {unscaled_pred}")
        return {"prediction": unscaled_pred}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root():
    return {"message": "FastAPI app is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
