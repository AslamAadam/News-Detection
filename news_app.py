# -*- coding: utf-8 -*-
# Streamlit deployment code
import streamlit as st
import pickle
import time

def main():
    st.set_page_config(
        page_title="News Detection App",
        page_icon="📰",  # You can use emojis or a URL to an image
        layout="wide",  # Optional: "centered" or "wide"
        initial_sidebar_state="expanded"  # Optional: "auto", "expanded", or "collapsed"
    )
    st.markdown(
        """
        <h1 style='text-align: center; color: #ffffff;'>
        📰 News Detection App
        </h1>
         """,
        unsafe_allow_html=True
    )
    st.markdown(
    """
    <style>
    .stProgress > div > div > div > div {
        background-color: #4CAF50;  /* Green color */
    }
    </style>
    """,
    unsafe_allow_html=True,
    )
    with st.sidebar:
        st.header("About")
        st.write("This app detects whether a news article is real or fake using a machine learning model.")
        st.write("Enter the news text in the text area and click 'Analyze' to see the result.")
        st.markdown("---")
        st.write("Developed by [Your Name]"
        )
    st.markdown("---")
    st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        © 2023 News Detection App. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown(
    """
    <style>
    .stTextArea > div > div > textarea {
        background-color: #f0f0f0;  /* Light gray background */
        border-radius: 10px;        /* Rounded corners */
        padding: 10px;              /* Padding inside the text area */
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://via.placeholder.com/1920x1080");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
        [theme]
        primaryColor = "#4CAF50"
        backgroundColor = "#FFFFFF"
        secondaryBackgroundColor = "#F0F2F6"
        textColor = "#262730"
        font = "sans serif"
    st.image("https://via.placeholder.com/150", width=150)  # Replace with your logo URL
    st.title("News Detection")
    with open('random_forest_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)

    # User input
    user_input = st.text_area("Enter news text to analyze:")

    if st.button("Analyze"):
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
                my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(0.1)
                my_bar.empty()
        
    if user_input.strip():
    # Transform user input
        input_vectorized = vectorizer.transform([user_input])
        # Predict
        prediction = model.predict(input_vectorized)[0]
        # Display result
        if prediction == 1:
            st.success("This news is Real.")
        else:
            st.error("This news is Fake.")
    else:
        st.warning("Please enter some text.")
    st.markdown(
        """
        <style>
        .stProgress > div > div > div > div {
        background-color: green;
        }
        </style>""",
        unsafe_allow_html=True,)        

if __name__ == "__main__":
    main()
