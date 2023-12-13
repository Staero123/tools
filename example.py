import streamlit as st
import mysql.connector


@st.cache_resource
def init_connection():
  return mysql.connector.connect(**st.secrets["mysql"]_
conn = init_connection()


st.title('Tools Log')

Tools_ID_input = st.text_area('Tools Id')
st.markdown(f"Tools ID is : {Tools_ID_input} ")
Employee_ID_input = st.text_area('Employee Id')
st.markdown(f"Employee ID is : {Employee_ID_input} ")
