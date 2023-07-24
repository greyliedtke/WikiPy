import streamlit as st
from NYT_CNXN.nyt_connection import NYTDBConnection

import pandas as pd

conn = st.experimental_connection("NYT", type=NYTDBConnection)

st.markdown("# NYT CNXN")

st.markdown("Example responses to the [pynytimes](https://pypi.org/project/pynytimes/) API")

st.divider()
st_nytts = st.button("NYT Top Stories")
if st_nytts:
    st.dataframe(conn.query("top_stories"))
st.divider()

cols = st.columns(2)
with cols[0]:
    st_nytms = st.button("NYT Most Shared")
with cols[1]:
    st_ms_days = st.selectbox("Days", [1, 7, 30])
if st_nytms:
    st.dataframe(conn.query("most_shared", days=st_ms_days))

st.divider()
cols = st.columns(2)
with cols[0]:
    st_nytmv = st.button("NYT Most Viewed")
with cols[1]:
    st_mv_days = st.selectbox("Days", [1, 7, 30], key="mvd")
if st_nytms:
    st.dataframe(conn.query("most_viewed", days=st_mv_days))
