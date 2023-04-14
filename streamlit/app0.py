import streamlit as st

def somma(l1:float,l2:float):
    a = l1+l2
    return a 

def main():
    st.text("Ciao questo front-end funziona")
    # slider
    num1 = st.slider('Please inserisci lato1 rettangolo', 0, 100, 25)
    num2 = st.slider('Please inserisci lato2 rettangolo', 0, 100, 35)
    r = somma(num1,num1)

    st.write("la somma è ", r)

if __name__ == "__main__":
    main()