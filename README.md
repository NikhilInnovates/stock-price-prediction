## Project Structure
```
stock-price-prediction/
│
├── app.py                  # Streamlit frontend
├── main.py                 # FastAPI backend
├── Untitled0.ipynb         # Jupyter Notebook for data preprocessing, model training, and real-time data streaming
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Files to ignore in Git
├── transformer_stock_model.pth  # Pretrained model
└── scaler.save             # Scaler file
```

---

### Explanation of Files
1. **`Untitled0.ipynb`**:
   - This is the main Jupyter Notebook where you:
     - Fetch real-time stock data using **Finnhub API**.
     - Preprocess historical stock data using **Alpha Vantage API**.
     - Train the **Transformer-based model** using PyTorch.
     - Stream real-time stock data using **WebSocket**.
     - Save the trained model and scaler for deployment.

2. **`app.py`**:
   - The Streamlit frontend for user interaction.
   - Allows users to input historical stock prices and get predictions.
   - Displays real-time stock data using **Chart.js**.

3. **`main.py`**:
   - The FastAPI backend for serving predictions.
   - Handles POST requests to predict future stock prices.

4. **`requirements.txt`**:
   - Lists all Python dependencies required to run the project.

5. **`transformer_stock_model.pth`**:
   - The pre-trained Transformer model weights.

6. **`scaler.save`**:
   - The scaler used to normalize input data for the model.

7. **`.gitignore`**:
   - Specifies files and folders to ignore in Git (e.g., virtual environments, logs).

---

### Updated **README.md** File
Here’s the updated `README.md` file with the `.ipynb` file included in the **Project Structure** section:

---

# Stock Price Prediction App

![Stock Price Prediction](https://img.shields.io/badge/Stock-Price_Prediction-blue) ![Python](https://img.shields.io/badge/Python-3.8%2B-green) ![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-brightgreen) ![Streamlit](https://img.shields.io/badge/Streamlit-1.26.0-orange)

This project is a **Stock Price Prediction App** that uses a **Transformer-based machine learning model** to predict future stock prices based on historical data. It consists of:
- A **FastAPI backend** for serving predictions.
- A **Streamlit frontend** for user interaction.
- **Real-time data streaming** using WebSocket for live stock price updates.
- **Interactive visualizations** using Chart.js for real-time and historical data.

---

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- **Historical Price Prediction**: Predicts future stock prices based on historical data using a Transformer-based model.
- **Real-Time Data Streaming**: Uses WebSocket to stream live stock price updates from Finnhub.
- **Interactive Interface**: Easy-to-use Streamlit app for input and visualization.
- **Scalable Backend**: FastAPI backend for serving predictions and handling real-time data.
- **Machine Learning Model**: Uses a Transformer-based model built with PyTorch for accurate predictions.
- **Scaler Integration**: Scales input data for better model performance.
- **Interactive Visualizations**: Uses Chart.js for real-time and historical stock price charts.

---

## Installation

### Prerequisites
- Python 3.8+
- Git

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/NikhilInnovates/stock-price-prediction.git
   cd stock-price-prediction
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the pre-trained model and scaler files:
   - Place `transformer_stock_model.pth` (model weights) and `scaler.save` (scaler file) in the project root directory.

4. Set up API keys:
   - Get your **Finnhub API key** and **Alpha Vantage API key**.
   - Replace `your key` in the code with your actual API keys.

---

## Usage

### Running the Backend (FastAPI)
1. Start the FastAPI server:
   ```bash
   python main.py
   ```
2. The backend will be available at `http://localhost:8003`.

### Running the Frontend (Streamlit)
1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. The app will be available at `http://localhost:8501`.

### Making Predictions
1. Open the Streamlit app in your browser.
2. Enter historical stock prices (comma-separated) and the number of days to predict.
3. Click the **Predict** button to see the predicted stock price.

### Real-Time Data Streaming
1. The app uses WebSocket to stream live stock price updates from Finnhub.
2. Real-time data is displayed in the Streamlit app using Chart.js.

---

## Deployment

### Local Deployment
- Run the FastAPI backend and Streamlit frontend locally as described in the [Usage](#usage) section.

### Cloud Deployment
- Use services like **Heroku**, **Render**, or **Google Cloud** to deploy the app.
- Example for Heroku:
  1. Create a `Procfile`:
     ```
     web: uvicorn main:app --host 0.0.0.0 --port $PORT
     ```
  2. Push your code to Heroku:
     ```bash
     heroku create
     git push heroku main
     ```

---

## Project Structure
```
stock-price-prediction/
│
├── app.py                  # Streamlit frontend
├── main.py                 # FastAPI backend
├── Untitled0.ipynb         # Jupyter Notebook for data preprocessing, model training, and real-time data streaming
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Files to ignore in Git
├── transformer_stock_model.pth  # Pretrained model
└── scaler.save             # Scaler file
```

---

## Technologies Used
- **Python**: Primary programming language.
- **FastAPI**: Backend framework for serving predictions and handling real-time data.
- **Streamlit**: Frontend framework for user interaction.
- **PyTorch**: Machine learning framework for the Transformer model.
- **WebSocket**: For real-time data streaming.
- **Chart.js**: For interactive visualizations of real-time and historical data.
- **Ngrok**: For exposing local servers to the internet.
- **Git**: Version control system.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- Thanks to the open-source community for providing the tools and libraries used in this project.
- Special thanks to [PyTorch](https://pytorch.org/) and [FastAPI](https://fastapi.tiangolo.com/) for their amazing frameworks.
- Thanks to [Finnhub](https://finnhub.io/) for providing real-time stock market data.

---

## Contact
For questions or feedback, feel free to reach out:
- **Nikhil Innovates**: [GitHub](https://github.com/NikhilInnovates) | [Email](mailto:panchalnikhil1710@gmail.com)
