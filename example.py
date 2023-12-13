import streamlit as st
conn = st.connection('mysql', type='sql')



st.title('Tools Log')

Tools_ID_input = st.text_area('Tools Id')
st.markdown(f"Tools ID is : {Tools_ID_input} ")
Employee_ID_input = st.text_area('Employee Id')
st.markdown(f"Employee ID is : {Employee_ID_input} ")
