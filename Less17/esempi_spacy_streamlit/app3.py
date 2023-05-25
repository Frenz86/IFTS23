# python -m spacy download en_core_web_sm
# python -m spacy download en_core_web_lg

import spacy
import streamlit as st
from spacy_streamlit import visualize_parser

def main():
    st.set_page_config(layout="wide") 
    st.title("Visualizza Parser")
    
    DEFAULT_MODEL = "en_core_web_sm"
    DEFAULT_TEXT = "Bill Gates is not the CEO of Microsoft anymore"

    raw_text = st.text_area("Text to analyze", DEFAULT_TEXT, height=200)
    nlp = spacy.load(DEFAULT_MODEL)
    doc = nlp(raw_text)

    if st.button('Visualizza Parser'):
        visualize_parser(doc)
 #######################################################


if __name__ == "__main__":
    main()
 