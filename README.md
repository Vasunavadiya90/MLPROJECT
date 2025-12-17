#### End to End Machine Learning Project
# Student Exam Performance Indicator

This project implements a Machine Learning pipeline to predict student exam performance based on various demographic and educational factors. It provides multiple interfaces for interacting with the model, including  FastAPI, and Streamlit.

## Project Structure

The project is organized as follows:

```
mlproject-main/
├── src/                    # Source code for the ML pipeline
│   ├── components/         # Data ingestion, transformation, and model training
│   ├── pipeline/           # Inference and training pipelines
│   ├── exception.py        # Custom exception handling
│   ├── logger.py           # Logging configuration
│   └── utils.py            # Utility functions
├── artifacts/              # Stored model and preprocessor objects (.pkl)
├── notebook/               # Jupyter notebooks for EDA and experimentation
├── app.py                  # Flask web application
├── fastapi_app.py          # FastAPI web application
├── streamlit_app.py        # Streamlit dashboard
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup script
└── README.md               # Project documentation
```

## Features

- **End-to-End ML Pipeline**: Handles data ingestion, preprocessing (scaling, encoding), and model prediction.
- **Web Interfaces**:
  - **FastAPI**: Modern, high-performance API with auto-generated docs.
  - **Streamlit**: Interactive data dashboard for quick testing.
- **Robust Error Handling**: Custom exception management and logging.

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd mlproject-main
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### 1. Running the FastAPI App
The FastAPI implementation provides a REST API and a Swagger UI.

```bash
python fastapi_app.py
```
- API Docs (Swagger UI): `http://127.0.0.1:8000/docs`
- Application: `http://127.0.0.1:8000`

### 2. Running the Streamlit App
The Streamlit app offers an interactive UI for predicting scores.

```bash
streamlit run streamlit_app.py
```
- Access the app at: `http://localhost:8501`

## Data Pipeline Details

- **Data Ingestion**: Reads data from source (CSV/DB), performs train-test split.
- **Data Transformation**:
  - Handles missing values.
  - One-hot encodes categorical variables (Gender, Encryption, etc.).
  - Scales numerical features (Reading/Writing scores).
- **Model Training**: Trains multiple models (CatBoost, XGBoost, etc.) and selects the best performer.
- **Prediction**: Loads the saved `model.pkl` and `preprocessor.pkl` to generate predictions on new data.

## License

[MIT License](LICENSE)