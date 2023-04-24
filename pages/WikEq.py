import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from WikEq.DF.dfs import df_eq, df_eqv, df_eqd
from WikEq.pages_equation import equation_page
from WikEq.pages_categories import category_page
from WikEq.pages_dimensions import dimension_page
from wikeqfu import solved_eqt


query_params = st.experimental_get_query_params()

st.title('WikEq')
with st.expander("Discover"):
    search = st.text_input("Search")
    if search:
        # get equations with name or description
        search_eq = df_eq[df_eq["Name"].str.contains(search, case=False)]

    st.markdown("*Equation Categories*")
    eq_cats = sorted(df_eq["EQ_CAT"].unique())
    for e in eq_cats:
        st.markdown(f"- [{e} equations](/WikEq?Category={e})")

if "Equation" in query_params:
    equation_page(query_params["Equation"][0])
   

elif "Category" in query_params:
    category_page(query_params["Category"][0])

elif "Dimension" in query_params:
    dimension_page(query_params["Dimension"][0])


else:
    st.title("Example Equations")
    eqns = df_eq.sample(n=3)
    eqns = eqns[["Name", "Eqn"]].sort_values(by="Name").values.tolist()
    eqns = list(eqns)
    cols = st.columns(2)
    for e in eqns:
        name, link = e[0], e[0].replace(" ", "%20")
        eqn = e[1]
        with cols[0]:
            st.markdown(f"[{name}](/WikEq?Equation={link})")
        with cols[1]:
            st.markdown(f"$${eqn}$$")

