import streamlit as st
import joblib   
# Load model and vectorizer
vectorizer = joblib.load("feature_extraction.jb")
model = joblib.load('spam_model.jb')
st.title("SPAM EMAIL CLASSIFIER")         
st.write("Enter your Email text below to check whether it is Spam or Ham.") 
# Correct variable name
email_input = st.text_area("Email Text:", "")
if st.button("Check Email"): 
    if email_input.strip(): 
        # Transform input text
        transform_input = vectorizer.transform([email_input]) 
        # Predict
        prediction = model.predict(transform_input) 
        # Show result
        if prediction[0] == 1: 
            st.success("The Email is Ham!") 
        else: 
            st.error("The Email is Spam!") 
    else: 
        st.warning("Please enter some text to analyze.")
st.write("Developed by rithvin04")

