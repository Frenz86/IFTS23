# python -m spacy download en_core_web_sm
# python -m textblob.download_corpora
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import streamlit as st

def main():
    # st.set_page_config(layout="wide") 
    st.title("Sentiment Analysis with Textblob and streamlit")
    DEFAULT_MODEL = "en_core_web_sm"
    DEFAULT_TEXT = 'I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy.'

    nlp = spacy.load(DEFAULT_MODEL)
    nlp.add_pipe('spacytextblob')
    raw_text = st.text_area("Text to analyze", DEFAULT_TEXT, height=200)
    doc = nlp(raw_text)

    st.write('Polarity:', round(doc._.blob.polarity, 2))
    st.write('Subjectivity:', round(doc._.blob.subjectivity, 2))

if __name__ == "__main__":
    main()
 