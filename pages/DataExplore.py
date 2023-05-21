"""
Script to create a figure from uploaded dataset
"""

# imports
import streamlit as st
import Ref
import pandas as pd
import altair as alt
import numpy as np
import plotly.figure_factory as ff

Ref.page_config()


st.title("Data Explorer")

user_file = st.file_uploader("Upload CSV")
st.divider()

if user_file:
    print("success")
else:
    x = np.array(range(0, 10))
    y1 = x*2
    y2 = x*3

    df = pd.DataFrame({'x': x, 'y1': y1, 'y2':y2})
    c = alt.Chart(df).mark_circle().encode(
    x='x', y='y1')
    st.altair_chart(c, use_container_width=True)
