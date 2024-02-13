import streamlit as st
import pandas as pd
import numpy as np
import csv
import requests

#this creates a title for the page
st.title('Pokemon Data Visualization tool')
st.divider()
# st.subheader('Pokemon Name')

#how to read csv files here 
# @st.cache_data  #we store/save this on the cache for faster access
# def load_data():
#     data=pd.read_csv('pokemon.csv')
#     return data
# data=load_data()

# #sidebar --ignore for now
# # st.sidebar.title('filters')
# # st.sidebar.subheader('select the type of pokemon')
# # types=data['Type 1'].unique()

# #create a dataframe with the pokemon data --check many more attributes for this func. in documentation
# st.dataframe(data=data)

#fetching data for the ditto pokemon from an api using url requests
def get_pokemon_data() ->dict:
    try:
        url="https://pokeapi.co/api/v2/pokemon/ditto"
        response=requests.get(url)
        data=response.json()
    except Exception as e:
        st.write(f'Error: {e}')
        data=None
    return data

pokemon_data=get_pokemon_data()

if pokemon_data:
    #if you try to display the data having different length of json dictonaries then you can print an error to the user like below 
    # # Attempt to convert JSON dictionary to DataFrame
    # try:
    #     df = pd.DataFrame.from_dict(pokemon_data)
    #     # Display the DataFrame if conversion succeeds
    #     st.dataframe(df)
    # except ValueError as e:
    #     # Display an error message if conversion fails
    #     st.error(f"Error: Unable to create DataFrame - {str(e)}")
    st.write('Pokemon data retrieved successfully')
    #just random info display
    st.header(pokemon_data.get('name'))
    st.subheader(pokemon_data.get('weight'))
    #sprites is the sub-dict and it contains the url in the 'front default' key
    st.image(pokemon_data.get('sprites').get('front_default'))

