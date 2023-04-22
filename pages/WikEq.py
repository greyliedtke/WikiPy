import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from WikEq.DF.dfs import df_eq, df_eqv, df_eqd

st.title('WikEq')
query_params = st.experimental_get_query_params()

with st.expander("Equation Categories"):
    eq_cats = sorted(df_eq["EQ_CAT"].unique())
    for e in eq_cats:
        st.markdown(f"[{e}](/WikEq?Category={e})")


if "Equation" in query_params:
    
    eq_name = query_params["Equation"][0]
    eq = df_eq[df_eq['Name']==eq_name]
    eqj = eq.to_dict('records')[0]
    st.title(eq_name)
    st.markdown(f"$$ {eqj['Eqn']} $$")
    st.markdown(eqj['Short_Desc'])
    st.markdown(f"- [Wikipedia]({eqj['WIKI_LINK']})")
    st.markdown(f"- [{eqj['EQ_CAT']} equations](/WikEq?Category={eqj['EQ_CAT']})")

    
    eq_vars = df_eqv[df_eqv['EQ_id']==int(eq['EQ_id'])].sort_values(by=['Symbol'])
    
    v_table = eq_vars[['Symbol', 'Short_Desc', 'SI_Units']]
    eq_vars
    v_table = v_table.set_index('Symbol')

    
    st.title("Equation Variables")
    st.dataframe(v_table)
    print('ok')

    # st.title("Symbolic Solving")
    # st.markdown(f"$$ {eq_vars.iloc[0]['Solved']} $$")

    # eqv = sorted(eq_vars['Symbol'].unique())
    # eqv_d = eq_vars.to_dict('records')
    # dim_links = sorted(eq_vars['D_Name'].unique())

if "Category" in query_params:
    category = query_params["Category"][0]

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

    st.dataframe(eqns)


    for i,row in eqns.iterrows():
        st.markdown(f"[{row['Name']}](/WikEq?Equations={row['Name']}) : $$ {row['Eqn']} $$")

    
# st.title("Equation Categoreis")





# eqns = df_eq.sample(n=3)
# eqns = eqns[["Name", "Eqn"]].sort_values(by="Name")
# for i,row in eqns.iterrows():
#     st.markdown(f"[{row['Name']}:{row['Eqn']}](/WikEq?Equation={row['Name']})")



# st.write(query_params)

# st.markdown('[Main](/WikEq?Equation=linked)')

# st.title("Equation categories")
# eq_cats = sorted(df_eq["EQ_CAT"].unique())
# for e in eq_cats:
#     st.markdown(f'[{e}](/WikEq?Equation={e})')
