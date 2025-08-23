# House Price Prediction Project

This project is an end-to-end machine learning application that predicts house prices based on various features.
It includes a Jupyter Notebook for data analysis and model training, and a Python web application to serve the final prediction model.

### Key Features
- **Data Analysis:** Exploratory Data Analysis (EDA) to understand feature distributions and correlations.
- **Model Training:** An XGBoost Regressor model is trained on the dataset to predict prices.
- **Web Application:** A simple web interface to input house features and receive a price prediction.

### Technologies Used
- Python
- Pandas & NumPy (for data manipulation)
- Scikit-learn (for data preprocessing)
- XGBoost (for the prediction model)
- Joblib (for saving the model)
- Flask / Streamlit (for the web application)

### Setup and Installation
1.  Clone the repository:
    `git clone https://github.com/your-username/your-repository-name.git`
2.  Navigate into the project directory:
    `cd your-repository-name`
3.  Install the required libraries:
    `pip install -r requirements.txt`

### Usage
- **To explore the analysis and model training process:**
  Open and run the `app.ipynb` Jupyter Notebook.
- **To run the web application:**
  `python app.py`
  Then, open your web browser and go to `http://127.0.0.1:5000`.
