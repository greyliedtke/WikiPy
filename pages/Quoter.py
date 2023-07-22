# page for displaying quotes

import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.markdown("# Quotes")

st.markdown(
    "[Contribute](https://forms.gle/H6aVkxk1ntaRAiRX7) to the log! Allow several minutes to update"
)

url = "https://docs.google.com/spreadsheets/d/1z49yYw1XBOccYkBhr0ZHTdY-YDqOBZMh7ci2bJTh7fI/edit?usp=sharing"
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
quotes = conn.read(spreadsheet=url, usecols=[1, 2, 3])

st.divider()
for i, q in quotes.iterrows():
    st.markdown(f"*{q['Author']}*")
    st.markdown(f"{q['Quote']}")
    st.divider()

with st.expander("QuoTable"):
    st.dataframe(quotes)

with st.expander("GSheets Experimental Connection Instructions"):
    st.code("""
            # only 3 lines of code!!
        url = "https://docs.google.com/spreadsheets/d/1z49yYw1XBOccYkBhr0ZHTdY-YDqOBZMh7ci2bJTh7fI/edit?usp=sharing"
        conn = st.experimental_connection("gsheets", type=GSheetsConnection)
        quotes = conn.read(spreadsheet=url, usecols=[1, 2, 3])
        """, language="python"
    )
