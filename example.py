import streamlit as st
 
st.title('Tools Log')

Tools_ID_input = st.text_area('Tools Id','Employee ID')
st.markdown(f"Tools ID is : {Tools_ID_input} ")

