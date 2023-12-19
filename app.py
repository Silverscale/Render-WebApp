# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('./IMDbMovies_clean.csv')
