import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

def get_fruitvice_data(this_fruit_choise):
  fruityvice_response =requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

def get_fruit_load_list():
  whit my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
 
def insert_row_sbowflake(new_fruit):
  whit my_cnx.cursor() as my_cur:
    my_cur.execute(f"insert into fruit_load_list values({new_fruit})")
    return "Thanks for adding " + new fruit
    

streamlit.title("My Parents New Healthy Diner")
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index),["Avocado", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the table on the page
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    streamlit.dataframe(get_fruitvice_data(fruit_choice))
except URLError as e:
  stramlit.error()
 

streamlit.header("the fruit load list contains:")

if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  streamlit.dataframe(get_fruit_load_list())


add_my_fruit = streamlit.text_input('What fruit would you like add?')
if streamlit.button('What fruit would you like to add?'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  streamlit.text(insert_row_sbowflake(add_my_fruit))
