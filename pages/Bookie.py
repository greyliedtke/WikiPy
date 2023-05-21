"""
page for book summaries quickly and in authors tone
"""

import streamlit as st
import pandas as pd
import Ref

Ref.page_config()
df = pd.read_json("Bookie/books.json", orient='index')

query_params = st.experimental_get_query_params()

# if book has been selected
if "Book" in query_params:
    book = query_params["Book"][0]
    st.markdown(f"# *{book}*")
    selected = df.loc[book]
    st.markdown(f"**{selected['author']}**")
    st.markdown(f"Rank: {selected['Rank']}")
    st.markdown(f"{selected['summaries']}")

    st.markdown(
        "<a href='Bookie' target = '_self'>Top 100 Books</a>",
        unsafe_allow_html=True,
    )


# list of 100 books
else:
    st.title("Top 100 Books")
    st.markdown("*According to [goodreads](https://www.goodreads.com/list/show/2681.Time_Magazine_s_All_Time_100_Novels)")
    dfv = df[['Rank', 'author']]
    for book, row in dfv.iterrows():
        book_link = book.replace(" ", "%20")
        book_link = book.replace("'", "%27")
        r, a = row["Rank"], row["author"]
        st.markdown(f"{r}. <a href='Bookie?Book={book_link}' target = '_self'>{book}</a> - {a}", unsafe_allow_html=True)

