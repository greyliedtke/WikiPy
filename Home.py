"""
streamlit run Home.py
"""



import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PyMakers",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# hide style...
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


st.title('Streamlit Wiki')
st.header("Do things here")

