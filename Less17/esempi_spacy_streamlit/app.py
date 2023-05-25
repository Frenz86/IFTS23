# python -m spacy download en_core_web_sm
import spacy
import spacy_streamlit
import streamlit as st

def main():
    # st.set_page_config(layout="wide") 
    st.title("App Tokenization")
    DEFAULT_MODEL = "en_core_web_sm"
    DEFAULT_TEXT = "this is a test"

    nlp = spacy.load(DEFAULT_MODEL)
    raw_text = st.text_area("Text to analyze", DEFAULT_TEXT, height=200)
    doc= nlp(raw_text)

    if st.button("tokenize"):
        spacy_streamlit.visualize_tokens(doc)

    # if st.button("Similarity"):
    #     spacy_streamlit.visualize_similarity(doc)

if __name__ == "__main__":
    main()