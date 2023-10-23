import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


#  col1, col2, col3 = st.columns(3)
# col1.metric("Name", 'a')
# col2.metric("Marks", 90)



a ={
    'name':['abc' , 'xyz'],
    'marks': [98,90]
} 
# Mining your data
df = pd.read_csv('marks1.csv')
st.title('This is  Data Mining')
if st.sidebar.button('Waiting'):df

# st.dataframe(df)
# st.dataframe(df,height=300, width=500)
st.table(df)# we cant take height width in table
# st.write(a)


# if st.button('Waiting'):df

st.table(a)


#  plots


# a1 = pd.DataFrame(df['Name'], df['Hindi'])
# st.line_chart(a1)

fig = plt.figure(figsize=(5,3))
# plt.plot(df['Name'], df['Hindi'])
if st.button('Loand BarChart'):df

plt.bar(df['Name'], df['Hindi'])
# plt.show()
st.pyplot(fig)

if st.sidebar.button('hello'): df
