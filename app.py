import streamlit as st
import requests

# Streamlit App
st.title("Named Entity Recognition")

# Text area for user input
sample_sentence = st.text_area("Enter a sample sentence:", "")

# Button to trigger named entity recognition
if st.button("Recognize Entities"):
    # API URL and headers
    API_URL = "https://api-inference.huggingface.co/models/spacy/en_core_web_sm"
    headers = {"Authorization": "Bearer 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"}

    # Function to make API call
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    # Perform API call for named entity recognition
    output = query({"inputs": sample_sentence})

    # Extract and display word and entity group tag pairs
    st.write("Word-Entity Group Pairs:")
    for entity in output:
        word = entity['word']
        entity_group = entity['entity_group']
        # Convert the first letter to uppercase and the rest to lowercase
        word = word.title()
        st.write(f"{word} - {entity_group}")

# Hide the GitHub icon with CSS
hide_github_css = """
<style>
.stActionButton{
    display: none !important;
}
</style>
"""
st.markdown(hide_github_css, unsafe_allow_html=True)
