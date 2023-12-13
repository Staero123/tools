import streamlit as st
import pandas as pd
import mysqlclient

def app():
    conn = mysql.connector.connect( host="localhost",
                                    port="3307",
                                    user="root",
                                    passwd="70013029",
                                    db="asset management"
                                  )

st.title('Tools Log')
Tools_ID_input = st.text_area('Tools Id')
st.markdown(f"Tools ID is : {Tools_ID_input} ")
Employee_ID_input = st.text_area('Employee Id')
st.markdown(f"Employee ID is : {Employee_ID_input} ")
