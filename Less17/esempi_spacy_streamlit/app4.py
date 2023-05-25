# python -m spacy download en_core_web_sm
import spacy
import streamlit as st
from itertools import combinations 
from spacy_streamlit import visualize_similarity
import pandas as pd

def main():
    st.set_page_config(layout="wide") 
    st.title("Similarity words streamlit")
    DEFAULT_MODEL = "en_core_web_sm"

    nlp = spacy.load(DEFAULT_MODEL)

    col1, col2= st.columns(2)
    with col1:
        word_1 = st.text_input('Parola 1', 'pizza')
    with col2:
        word_2 = st.text_input('Parola 2', 'fries')
    
    nlplg=spacy.load("en_core_web_lg")
    visualize_similarity(nlplg, (word_1, word_2))

#########################################à
    col1, col2, col3 = st.columns(3)
    with col1:
        word_1 = st.text_input('Parola 1', 'shirt')
    with col2:
        word_2 = st.text_input('Parola 2', 'jeans')
    with col3:
        word_3 = st.text_input('Parola 3', 'apple')

    tokens = nlp(f"{word_1} {word_2} {word_3}")

    # get combination of tokens
    comb = combinations(tokens, 2)

    most_similar = 0
    match_tokens = None
    compared_tokens = []
    similarities = []
    for token in list(comb):
        similarity = token[0].similarity(token[1])
        compared_tokens.append(token)
        similarities.append(similarity)
        if similarity > most_similar:

            most_similar = similarity
            match_tokens = token

    if st.button('similarities'):
        st.write(f'{match_tokens[0]} and {match_tokens[1]} are the most similar with a similarity of {round(most_similar*100, 2)}%')
        st.write('## Results')

        dictio = {
                'Tokens': [compared_tokens[0],compared_tokens[1],0],
                'Similarity': [similarities[0],similarities[1],similarities[2]]
                }
        
        df = pd.DataFrame(dictio).sort_values(by='Similarity', ascending=False)
        st.dataframe(df)
        st.write(dictio)


if __name__ == "__main__":
    main()
 