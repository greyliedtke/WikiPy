import theme
from nicegui import ui
from WikEq.DF.dfs import df_eq, df_eqv, df_eqd



eq_v_cols = [
    {'name': 'dimension', 'label': 'Dimension', 'field': 'D_Name'},
    {'name': 'symbol', 'label': 'Symbol', 'field': 'Symbol'},
    {'name': 'units', 'label': 'SI Units', 'field': 'SI_Units'},
    {'name': 'short_desc', 'label': 'Description', 'field': 'Short_Desc'},
]

@ui.page('/WikEq/Equations/{eq_name}')
def WikEq(eq_name: str):

    theme.add_header()
    with theme.row():
        eq = df_eq[df_eq['Name']==eq_name]
        eqj = eq.to_dict('records')[0]
        eq_vars = df_eqv[df_eqv['EQ_id']==int(eq['EQ_id'])].sort_values(by=['Symbol'])

        # variable table
        eqv_d = eq_vars.to_dict('records')
        ui.table(columns=eq_v_cols, rows=eqv_d, row_key='name', title='Equation Variables')

        dim_links = sorted(eq_vars['D_Name'].unique())
        # print(dim_links)
        for d in dim_links:
            ui.link(d, '/WikEq/Dimensions/'+ d)

    with theme.row():
        ui.markdown('## Solving')
        ui.label(eq_vars)
        eqv = sorted(eq_vars['D_Name'].unique())

        def update_eq_solve():
            selected = str(select1.value)
            new_a = eq_vars[eq_vars['D_Name'] == selected]
            solved_label.text = str(new_a['Solved'].values[0])

        select1 = ui.select(eqv, value=eqv[0], on_change=lambda : update_eq_solve())
        solved_label = ui.label(eq_vars.iloc[0]['Solved'])
        
    with theme.row():
        ui.markdown('## Equation')
        ui.markdown(f"### {eqj['Eqn']}")
        ui.label(eqj['Name'])
        ui.label(eqj['Short_Desc'])
        ui.link('Wiki Link', eqj['WIKI_LINK'])
        ui.link(eqj['EQ_CAT']+' Equations', '/WikEq/Categories/'+eqj['EQ_CAT'])

