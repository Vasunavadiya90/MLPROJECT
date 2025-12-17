import streamlit as st
import requests
import json

def main():
    st.set_page_config(page_title="Student Exam Performance Prediction", layout="centered")
    
    st.title("Student Exam Performance Indicator")
    st.markdown("Enter student details to predict their math score.")
    
    # Form Inputs
    with st.form("prediction_form"):
        gender = st.selectbox("Gender", ["male", "female"])
        
        race = st.selectbox("Race or Ethnicity", [
            "group A", "group B", "group C", "group D", "group E"
        ])
        
        parental_level_of_education = st.selectbox("Parental Level of Education", [
            "associate's degree",
            "bachelor's degree",
            "high school",
            "master's degree",
            "some college",
            "some high school"
        ])
        
        lunch = st.selectbox("Lunch Type", ["free/reduced", "standard"])
        
        test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
        
        reading_score = st.number_input("Reading Score (0-100)", min_value=0, max_value=100, value=50)
        writing_score = st.number_input("Writing Score (0-100)", min_value=0, max_value=100, value=50)
        
        submit_button = st.form_submit_button("Predict Math Score")
        
    if submit_button:
        # Prepare data payload
        data = {
            "gender": gender,
            "race_ethnicity": race,
            "parental_level_of_education": parental_level_of_education,
            "lunch": lunch,
            "test_preparation_course": test_preparation_course,
            "reading_score": reading_score,
            "writing_score": writing_score
        }
        
        # Make API request to FastAPI backend
        try:
            # Assuming backend is running on default port 8000
            response = requests.post("http://127.0.0.1:8000/predict", json=data)
            
            if response.status_code == 200:
                result = response.json()
                prediction = result["prediction"]
                st.success(f"The predicted Math Score is: {prediction:.2f}")
            else:
                st.error(f"Error: {response.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the backend server. Is it running?")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
