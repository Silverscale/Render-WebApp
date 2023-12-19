# Sprint6
Web App for the 6th sprint in the TripleTen DA course.

This project uses a DataSet on IMDb Movies that can be found on Kaggle.com, to analyze the evolution of movies and the relationship on budget, ratings and revenue.

Libraries:
 - pandas
 - streamlit
 - plotly.express
 - altair

It consists on:
 1- a jupyter notebook (EDA.ipynb) were we carry out the Data preprocessing and initial analysis.
 2- a web app (app.py) made with streamlit.
 
##How to use it

To open the jupyter notebook, you can visit jupyter.org and either install it or try it online. You need both the notebook (EDA.ipynb) and the DataSet (IMDbMovies.csv) in the proper file structure:

\Notebook\EDA.ipynb
\IMDbMovies.csv

To open the web app, you need to set up a Python environment (this project was made with version 3.9.18) and install the libraries mentioned above. Then run the app with the command:
    streamlit run app.py
This will open the app in your web browser.