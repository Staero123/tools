import streamlit as st
import pandas as pd
import mysql.connector

st.title('Tools Log')
Tools_ID_input = st.text_area('Tools Id')
st.markdown(f"Tools ID is : {Tools_ID_input} ")
Employee_ID_input = st.text_area('Employee Id')
st.markdown(f"Employee ID is : {Employee_ID_input} ")


conn = mysql.connector.connect(host="localhost",port="3307",user="root",passwd="70013029",db="asset management")
cursor = conn.cursor()
cursor.execute('INSERT INTO main (EmployeeID,ToolsID,Check_In_Time,LogID) VALUES (%s,%s,%s,%s)',(Employee_ID_input,Tools_ID_input,now.strftime('%Y-%m-%d %H:%M:%S'),2))
conn.commit()
conn.close()


