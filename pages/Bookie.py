"""
page for book summaries quickly and in authors tone
"""

import streamlit as st
import pandas as pd


st.title("Top 100 Books")
df = pd.read_json("Bookie/books.json", orient='index')

cols = st.columns(2)
with cols[0]:
    dfv = df[['Rank', 'author']]
    dfv.index.name = "Title"
    st.dataframe(dfv)
with cols[1]:
    book = st.selectbox("Select Book", options=list(df.index))
    st.markdown("[GoodReads Source](https://www.goodreads.com/list/show/2681.Time_Magazine_s_All_Time_100_Novels)")
    st.markdown("Summaries generated via openAI model to summarize storty, theme and writing style without spoiling")

if book:
    st.title(book)
    st.markdown(f"By: {df.loc[book]['author']}")
    st.markdown(f"Summary: \n\n {df.loc[book]['summaries']}")
