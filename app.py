# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('./IMDbMovies_clean.csv')

st.header('IMDbMovies')
st.write("Let's take a look at the cinematographic industry's evolution over the years")
st.subheader('Increasing production costs')
st.write('We all know that making movies has become increasingly expensive.', \
         '\nHow much? And was it worth it? ')

# a budget of 0 means the data is missing from our DataSet
filtered_budget = df[df['budget_estimated'] != 0]
# It's quite hard to find exchange data from before 1990. We'll only use dollars
filtered_budget = filtered_budget[filtered_budget['currency'] == '$']


fig = px.histogram(filtered_budget, x='release_year', y='budget_estimated', histfunc='avg')
st.plotly_chart(fig)