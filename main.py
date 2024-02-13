import streamlit as st
import pandas as pd
#this creates a title for the page
st.title('Pokemon Data Visualization tool')
st.divider()
st.subheader('Pokemon Name')

#how to read csv files here 
@st.cache_data  #we store/save this on the cache for faster access
def load_data():
    data=pd.read_csv('pokemon.csv')
    return data
data=load_data()

#sidebar --ignore for now
# st.sidebar.title('filters')
# st.sidebar.subheader('select the type of pokemon')
# types=data['Type 1'].unique()

#create a dataframe with the pokemon data
st.dataframe(data=data,)
