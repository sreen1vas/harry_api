import streamlit as st
import requests

# FastAPI URL
API_URL = "http://127.0.0.1:8000/result"

# Streamlit UI
st.title("Harry Potter Q&A")
st.write("Ask a question about Harry Potter, and the app will fetch the answer from the FastAPI backend.")

# User input
question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if question.strip():
        # Make the request to the FastAPI endpoint
        response = requests.get(API_URL, params={"question": question})
        
        # Check if the request was successful
        if response.status_code == 200:
            answer = response.json()
            st.subheader("Answer:")
            st.write(answer)
        else:
            st.error(f"Error: Unable to fetch data. Status code {response.status_code}")
    else:
        st.warning("Please enter a valid question.")
