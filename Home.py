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
    initial_sidebar_state="collapsed",
)


c = st.container()
with c:
    st.markdown("## <a href='WikEq' target = '_self'>WikEQ</a>", unsafe_allow_html=True)
    st.markdown("- Symbolic solving equation wiki")
st.divider()

c = st.container()
with c:
    st.markdown(
        "## <a href='Bookie' target = '_self'>Top 100 Books</a>",
        unsafe_allow_html=True,
    )
    st.markdown("- Chat GPT summary of top 100 books from Goodreads")

st.divider()


# hide style...
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)
