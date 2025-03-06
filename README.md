# Stock Price Prediction App

![Stock Price Prediction](https://img.shields.io/badge/Stock-Price_Prediction-blue) ![Python](https://img.shields.io/badge/Python-3.8%2B-green) ![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-brightgreen) ![Streamlit](https://img.shields.io/badge/Streamlit-1.26.0-orange)

This project is a **Stock Price Prediction App** that uses a **Transformer-based machine learning model** to predict future stock prices based on historical data. It consists of:
- A **FastAPI backend** for serving predictions.
- A **Streamlit frontend** for user interaction.

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
- **Historical Price Prediction**: Predicts future stock prices based on historical data.
- **Interactive Interface**: Easy-to-use Streamlit app for input and visualization.
- **Scalable Backend**: FastAPI backend for serving predictions.
- **Machine Learning Model**: Uses a Transformer-based model for accurate predictions.
- **Scaler Integration**: Scales input data for better model performance.

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
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Files to ignore in Git
├── transformer_stock_model.pth  # Pretrained model
└── scaler.save             # Scaler file
```

---

## Technologies Used
- **Python**: Primary programming language.
- **FastAPI**: Backend framework for serving predictions.
- **Streamlit**: Frontend framework for user interaction.
- **PyTorch**: Machine learning framework for the Transformer model.
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

---

## Contact
For questions or feedback, feel free to reach out:
- **Nikhil Innovates**: [GitHub](https://github.com/NikhilInnovates) | [Email](mailto:panchalnikhil1710@gmail.com)

---

This `README.md` file provides a professional overview of your project, making it easy for others to understand, use, and contribute to your work. Let me know if you need further customization! 🚀
