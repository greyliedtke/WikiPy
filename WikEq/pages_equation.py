"""
script for creating equation page
"""

# imports
import streamlit as st
from WikEq.DF.dfs import df_eq, df_eqv, df_eqd


def solved_eqt(eq_vars, a):
    # function to convert equation variables into python solution...
    md_t = ""
    for v in eq_vars:
        if v == a:pass
        else:
            md_t += f"{v} = 1 \n"
    md_t += f"{eq_vars[a]['Solved']}"
    return md_t


def equation_page(eq_name):

    eq = df_eq[df_eq['Name']==eq_name]
    eqj = eq.to_dict('records')[0]


    st.title(eq_name)
    st.markdown(f"$$ {eqj['Eqn']} $$")
    st.markdown(eqj['Short_Desc'])
    st.markdown(f"- [Wikipedia]({eqj['WIKI_LINK']})")


    eq_vars = df_eqv[df_eqv['EQ_id']==int(eq['EQ_id'])].sort_values(by=['Symbol'])
    eq_vars = eq_vars.set_index('Symbol')
    
    st.title("Equation Variables")
    v_table = eq_vars[['Short_Desc', 'SI_Units']]
    st.dataframe(v_table)

    v_dict = eq_vars.to_dict(orient='index')
    st.title("Symbolic Solving")
    symbols = list(v_dict.keys())
    st.markdown(f"$$ {v_dict[symbols[0]]['Solved']} $$")

    solve_for = st.selectbox("Solve for", options=v_table.index)

    if solve_for:
        solve_t = solved_eqt(v_dict,solve_for)
        st.text_area("Code Solution", value=solve_t, height=200)


    # eqv = sorted(eq_vars['Symbol'].unique())
    # eqv_d = eq_vars.to_dict('records')
    # dim_links = sorted(eq_vars['D_Name'].unique())
