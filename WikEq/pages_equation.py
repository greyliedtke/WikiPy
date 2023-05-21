"""
script for creating equation page
"""

# imports
import streamlit as st
from WikEq.DF.dfs import df_eq, df_eqv, df_eqd


def solved_eqt(eq_vars, a):
    # function to convert equation variables into python solution...
    md_t = ""
    solution = eq_vars[a]['Solved']

    for v in eq_vars:
        if v == a:pass
        else:
            md_t += f"{v} = 1 # {eq_vars[v]['SI_Units']}\n"
    md_t += f"{eq_vars[a]['Solved']}"
    return md_t, solution 


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

    # with cols[1]:
    #     dim_links = sorted(eq_vars['D_Name'].unique())
    #     for d in dim_links:
    #         st.markdown(f"{d},")

    v_dict = eq_vars.to_dict(orient='index')
    st.title("Symbolic Solving")
    symbols = list(v_dict.keys())

    solve_for = st.selectbox("Solve for", options=v_table.index)

    if solve_for:
        solve_t, solution = solved_eqt(v_dict,solve_for)
        st.markdown(f"$$ {solution} $$")
        st.text_area("Code Solution", value=solve_t, height=200)


