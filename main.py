import streamlit as st
import pandas as pd
import numpy as np
import csv
import requests
from annotated_text import annotated_text


#colors-
colours = {
    'normal': '#A8A77A',
    'fire': '#EE8130',
    'water': '#6390F0',
    'electric': '#F7D02C',
    'grass': '#7AC74C',
    'ice': '#96D9D6',
    'fighting': '#C22E28',
    'poison': '#A33EA1',
    'ground': '#E2BF65',
    'flying': '#A98FF3',
    'psychic': '#F95587',
    'bug': '#A6B91A',
    'rock': '#B6A136',
    'ghost': '#735797',
    'dragon': '#6F35FC',
    'dark': '#705746',
    'steel': '#B7B7CE',
    'fairy': '#D685AD',
};
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
#get random pokedex number-
random_number=str(np.random.randint(1,1001))
random_number2=str(np.random.randint(1,1001))
def get_random_pokemon(number:int)->str:
    try:
        url="https://pokeapi.co/api/v2/pokemon-species/"+number
        response=requests.get(url)
        data=response.json()
    except Exception as e:
        st.write(f'Error: {e}')
        data=None
    return data.get("name")  #here we get a random pokemon's name 
poke_name=get_random_pokemon(random_number)
poke_name2=get_random_pokemon(random_number2)
#fetching data for the pokemon from an api using url requests
#this part is to get a pokemon's data specified with the url 
def get_pokemon_data(pokemon_name) ->dict:
    try:
        url="https://pokeapi.co/api/v2/pokemon/"+pokemon_name
        response=requests.get(url)
        data=response.json()
    except Exception as e:
        st.write(f'Error: {e}')
        data=None
    return data  #here we get the same random generated pokemon's data dictonary

pokemon_data=get_pokemon_data(poke_name)
pokemon_data2=get_pokemon_data(poke_name2)
#fetching two pokemon data and comparing them
if pokemon_data and pokemon_data2:
    col1,col2 = st.columns(2)
    with col1:
        st.header(pokemon_data.get('name').capitalize())
        #sprites is the sub-dict and it contains the url in the 'front default' key
        st.image(pokemon_data.get('sprites').get('front_default'))
        st.write('Pokemon Weight: ',pokemon_data.get('weight'))
        poke_type=pokemon_data.get('types')[0].get('type').get('name')
        #the tuple below takes 3 attributes -
        #1st is the main header/data 
        #2nd is the subheader/can be empty
        #3rd is the color
        annotated_text(  
        (f'Pokemon Type: {poke_type}',"",colours[poke_type])
        )
    with col2:
        st.header(pokemon_data2.get('name').capitalize())
        #sprites is the sub-dict and it contains the url in the 'front default' key
        st.image(pokemon_data2.get('sprites').get('front_default'))
        st.write('Pokemon Weight: ',pokemon_data2.get('weight'))
        poke_type=pokemon_data2.get('types')[0].get('type').get('name')
        #the tuple below takes 3 attributes -
        #1st is the main header/data 
        #2nd is the subheader/can be empty
        #3rd is the color
        annotated_text(  
        (f'Pokemon Type: {poke_type}',"",colours[poke_type])
        )
    # comparision={
    #     pokemon_data.get('name').capitalize():pokemon_data.get('height'),
    #     pokemon_data2.get('name').capitalize():pokemon_data2.get('height')
    # }
    # Create dictionary to store stats data for both Pokemon
    stats_data1 = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
    stats_data2 = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data2['stats']}

    # Create DataFrame from the stats data
    df_stats = pd.DataFrame([stats_data1, stats_data2])

    # Plot bar chart
    st.bar_chart(df_stats)












#if you try to display the data having different length of json dictonaries then you can print an error to the user like below 
    # # Attempt to convert JSON dictionary to DataFrame
    # try:
    #     df = pd.DataFrame.from_dict(pokemon_data)
    #     # Display the DataFrame if conversion succeeds
    #     st.dataframe(df)
    # except ValueError as e:
    #     # Display an error message if conversion fails
    #     st.error(f"Error: Unable to create DataFrame - {str(e)}")

    

