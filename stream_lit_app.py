import streamlit
streamlit.title('my parents new healthy diner')
streamlit.header('breakfast Favorites')

streamlit.text('🥣omega 3 & blueberry oatmeal')
streamlit.text('🥗 kale,spinach and rocket smoothie')
streamlit.text('🐔 hard boiled free-ragne eggs')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 build your own fruit smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
