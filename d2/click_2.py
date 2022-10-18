import streamlit as st
from streamlit_plotly_events import plotly_events
import plotly.express as px
import pandas as pd

# Writes a component similar to st.write()


x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
df=[]
df= pd.DataFrame(df)
df['year']= x
df['lifeExp']= y

# fig = px.line(x=[1], y=[1])

fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
selected_points = plotly_events(fig)

selected_points
# Can write inside of things using with!
# with st.beta_expander('Plot'):
#     fig = px.line(x=[1], y=[1])
#     selected_points = plotly_events(fig)
