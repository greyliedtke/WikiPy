import theme
from nicegui import ui
from WikEq.DF.dfs import df_eq, df_eqv, df_eqd



eq_v_cols = [
    {'name': 'symbol', 'label': 'Variable', 'field': 'Symbol'},
    {'name': 'units', 'label': 'SI Units', 'field': 'SI_Units'},
    {'name': 'short_desc', 'label': 'Description', 'field': 'Short_Desc'},
    {'name': 'dimension', 'label': 'Dimension', 'field': 'D_Name'}
]

def solved_eqt(eq_vars, a):
    md_t = ""
    for v in eq_vars:
        if v == a['Symbol'].values[0]:pass
        else:
            md_t += f"{v} = 1 \n"
    md_t += f"{a['Solved'].values[0]}"
    return md_t



@ui.page('/WikEq/Equations/{eq_name}')
def WikEq(eq_name: str):

    eq = df_eq[df_eq['Name']==eq_name]
    eqj = eq.to_dict('records')[0]
    eq_vars = df_eqv[df_eqv['EQ_id']==int(eq['EQ_id'])].sort_values(by=['Symbol'])
    eqv = sorted(eq_vars['Symbol'].unique())
    eqv_d = eq_vars.to_dict('records')
    dim_links = sorted(eq_vars['D_Name'].unique())

    theme.add_header()

# with theme.row():
    with theme.cc():
        ui.markdown(f"### {eqj['Name']}: <em>{eqj['Eqn']}</em>")
        ui.markdown(eqj['Short_Desc'])
        ui.markdown(f"- [Wikipedia]({eqj['WIKI_LINK']})")
        ui.markdown(f"- [{eqj['EQ_CAT']} equations](/WikEq/Categories/{eqj['EQ_CAT']})")

# with theme.row():
    with theme.cc():
        with ui.row():
            ui.table(columns=eq_v_cols, rows=eqv_d, row_key='name', title='Equation Variables')

            with theme.cc():
                ui.markdown('Dimension Pages for')
                for d in dim_links:
                    ui.markdown(f"- **[{d}](/WikEq/Dimensions/{d})**")

# with theme.row():
    with theme.cc():
        with ui.card().classes('bg-white'):
            def update_eq_solve():
                selected = str(select1.value)
                new_a = eq_vars[eq_vars['Symbol'] == selected]
                solved_md.content = f"### <em>{str(new_a['Solved'].values[0])}</em>"
                solved_txt.value = solved_eqt(eqv, new_a)

            ui.markdown('### Equation Solver')
            with ui.row():
                ui.markdown('#### Solving for: ')
                select1 = ui.select(eqv, value=eqv[0], on_change=lambda : update_eq_solve())
                select1.tailwind('text-xl')
            solved_md = ui.markdown(f"<em> **{eq_vars.iloc[0]['Solved']}</em>")
            solved_txt = ui.textarea().style("background-color: white;max-width: 1000px")
            update_eq_solve()