"""
script for creating dimension page
"""

# imports
import streamlit as st
from WikEq.DF.dfs import df_eq, df_eqv, df_eqd

def dimension_page(dimension):

    dim = df_eqd.loc[df_eqd['Base_quantity']== dimension]
    dimj = dim.to_dict('records')[0]

    cols = st.columns(2)
    with cols[0]:

        st.markdown(f'### {dimension}')
        st.markdown(f"- Symbol: {dimj['Symbol']}")
        st.markdown(f"- Description: {dimj['Description']}")
        st.markdown(f"- SI Base Units: {dimj['SI_base_unit']}")
        st.markdown(f"- Dimensionality: {dimj['Dimension']}")
        st.markdown(f"- [Wikipedia]({dimj['WIKI_LINK']})")

        # get all equations this id is found in
        eq_ids = df_eqv[df_eqv['D_Name'] == dimension]['EQ_id'].unique()
        eqs = df_eq.loc[df_eq['EQ_id'].isin(eq_ids), ['Name', 'Eqn']].sort_values(by="Name").values.tolist()

    with cols[1]:
        st.markdown('### Found in Equations: ')

        cols = st.columns(2)
        for e in eqs:
            eq_name = e[0]
            eq_link = eq_name.replace(" ", "%20")
            eq = e[1]
            with cols[0]:
                st.markdown(f"[{eq_name}](/WikEq?Equation={eq_link})")
                st.markdown(f"<a href='/WikEq?Equation={eq_link}' target = '_self'> {eq_name} </a>", unsafe_allow_html=True)
        
            with cols[1]:
                st.markdown(f"$$ {eq} $$")



