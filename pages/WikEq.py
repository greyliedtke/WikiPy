import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from WikEq.DF.dfs import df_eq, df_eqv, df_eqd
from WikEq.pages_equation import equation_page
from WikEq.pages_categories import category_page
from WikEq.pages_dimensions import dimension_page
from Ref import solved_eqt
import Ref

Ref.page_config()

query_params = st.experimental_get_query_params()

st.title('WikEq')
with st.expander("Discover"):
    search = st.text_input("Search")
    if search:
        # Equation Results
        search_names = df_eq[df_eq["Name"].str.contains(search, case=False)]
        if len(search_names)>0:
            st.markdown("**Matching equations:**")
            for e, row in search_names.iterrows():
                name, link = row["Name"], row["Name"].replace(" ", "%20")
                st.markdown(f"<a href='WikEq?Equation={link}' target = '_self'>{name}</a>", unsafe_allow_html=True)
        else:
            st.markdown("No matching equations...")
        # Dimension Results
        search_dims = df_eqd[df_eqd["Base_quantity"].str.contains(search, case=False)]
        if len(search_dims)>0:
            st.markdown("**Matching dimensions:**")
            for e, row in search_dims.iterrows():
                name, link = row["Base_quantity"], row["Base_quantity"].replace(" ", "%20")
                st.markdown(f"<a href='WikEq?Dimension={link}' target = '_self'>{name}</a>", unsafe_allow_html=True)
        else:
            st.markdown("No matching dimensions...")
    st.markdown("**Equation Categories**")
    eq_cats = sorted(df_eq["EQ_CAT"].unique())
    for e in eq_cats:
        st.markdown(f"<a href='WikEq?Category={e}' target = '_self'>{e} equations</a>", unsafe_allow_html=True)

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
            st.markdown(f"<a href='WikEq?Equation={link}' target = '_self'>{name}</a>", unsafe_allow_html=True)
        with cols[1]:
            st.markdown(f"$${eqn}$$")

