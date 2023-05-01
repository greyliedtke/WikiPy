"""
page for book summaries quickly and in authors tone
"""

import streamlit as st
import pandas as pd


df = pd.read_json("Bookie/books.json", orient='index')

query_params = st.experimental_get_query_params()


if "Book" in query_params:
    st.markdown("# Bookie Summary")
    book = query_params["Book"][0]
    st.markdown(f"# *{book}*")
    selected = df.loc[book]
    print(selected)
    st.markdown(f"**{selected['author']}**")
    st.markdown(f"Rank: {selected['Rank']}")
    st.markdown(f"{selected['summaries']}")

    st.divider()

    next_b = int(selected["Rank"])+1
    nb = df.iloc[next_b]
    nb_name = nb["Book"].replace(" ", "%20")

    st.markdown(f"[Main](/Bookie)")
    st.markdown(f"[Next](/Bookie?Book={nb_name})")

   
else:
    st.title("Top 100 Books")
    dfv = df[['Rank', 'author']]
    dfv.index.name = "Title"
    st.dataframe(dfv)

    st.divider()
    book = "To Kill a Mockingbird"
    book_link = book.replace(" ", "%20")
    st.markdown(f"[{book}](/Bookie?Book={book_link})")
    st.divider()

    book = st.selectbox("Select Book", options=list(df.index))
    st.markdown("[GoodReads Source](https://www.goodreads.com/list/show/2681.Time_Magazine_s_All_Time_100_Novels)")
    st.markdown("Summaries generated via openAI model to summarize storty, theme and writing style without spoiling")
