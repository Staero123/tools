import streamlit as st
 
st.title('My First Streamlit App')

text_input = st.text_input('Tools Id', )
st.markdown(f"Tools ID is : {text_input} ")
