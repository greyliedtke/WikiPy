import theme
from nicegui import ui
from WikEq.DF.dfs import df_eq, df_eqv, df_eqd


@ui.page('/WikEq/Dimensions')
def WikEq():
    theme.add_header()
    with theme.row():
        theme.title('WikEq Dimensions')
        theme.subtitle('A symbolic solving and dimension referencing equation wiki.')

    with theme.row():
        with theme.cc():
            dims = df_eqd[['Base_quantity', 'Description']].sort_values(by='Base_quantity')
            for i, row in dims.iterrows():
                ui.link(row['Base_quantity'], '/WikEq/Dimensions/'+row['Base_quantity'])


# ----------------------------------------------
@ui.page('/WikEq/Dimensions/{dimension}')
def WikEq(dimension):
    theme.add_header()
    # with theme.row():
    # get all equations with blah
    dim = df_eqd.loc[df_eqd['Base_quantity']== dimension]
    dimj = dim.to_dict('records')[0]

    with theme.cc():
        ui.markdown(f'### {dimension}')
        ui.markdown(f"- Symbol: {dimj['Symbol']}")
        ui.markdown(f"- Description: {dimj['Description']}")
        ui.markdown(f"- SI [Base Units](/WikEq/###Base%20Dimensions): {dimj['SI_base_unit']}")
        ui.markdown(f"- Dimensionality: {dimj['Dimension']}")
        ui.markdown(f"- [Wikipedia]({dimj['WIKI_LINK']})")

    # get all equations this id is found in
    eq_ids = df_eqv[df_eqv['D_Name'] == dimension]['EQ_id'].unique()
    eqs = df_eq.loc[df_eq['EQ_id'].isin(eq_ids), ['Name', 'Eqn']].sort_values(by="Name").values.tolist()
    with theme.cc():
        ui.markdown('### Found in Equations: ')
        for e in eqs:
            ui.markdown(f"- [{e[0]}](/WikEq/Equations/{e[0]}): <em>{e[1]}</em>")
