"""
script for creating equation page
"""

# imports
import streamlit as st
from WikEq.DF.dfs import df_eq, df_eqv, df_eqd

def category_page(category):

    st.markdown(f"{category} Equations")

    eqns = df_eq.loc[df_eq["EQ_CAT"] == category]
    eqns = eqns[["Name", "Eqn"]].sort_values(by="Name")
    eqns_d = eqns.to_dict(orient='records')
    cols = st.columns(2)
    for e in eqns_d:
        eq_name = e['Name']
        link = eq_name.replace(" ", "%20")
        with cols[0]:
            st.markdown(f"[{eq_name}](/WikEq?Equation={link})")
        with cols[1]:
            st.markdown(f"$$ {e['Eqn']} $$")



