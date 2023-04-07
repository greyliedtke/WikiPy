from nicegui import ui
from WikEq.DF.dfs import df_eq, df_eqv, df_eqd
import theme
from nicegui import Tailwind, ui
import WikEq.page_equations, WikEq.page_dimensions

columns = [
    {'name': 'dimension', 'label': 'Dimension', 'field': 'name', 'required': True, 'align': 'left'},
    {'name': 'units', 'label': 'SI Units', 'field': 'units', 'sortable': True},
]
rows = [
    {'name': 'Length', 'units': 'm'},
    {'name': 'Mass', 'units': 'kg'},
    {'name': 'Time', 'units': 's'},
    {'name': 'Electric Current', 'units': 'A'},
    {'name': 'Temperature', 'units': 'K'},
    {'name': 'Amount of substance', 'units': 'mol'},
    {'name': 'Luminosity', 'units': 'cd'},
]

@ui.page('/WikEq')
def WikEq():
    theme.add_header()
    with theme.row():
        theme.title('*WikEQ*')
        theme.subtitle('A symbolic solving and dimension referencing equation wiki.')

    with theme.row():
        with ui.card():
            ui.markdown('### Equation Categories')
            ui.markdown('Explore equations in certain categories')

            # get unique equation categories
            eq_cats = sorted(df_eq['EQ_CAT'].unique())
            with ui.expansion('Categories'):
                for e in eq_cats:
                    ui.link(e, '/WikEq/Categories/'+e)
                    ui.markdown('')

    with theme.row():
        with ui.card():
            ui.markdown('### Base Dimensions')
            ui.markdown('All dimensions originate from the 7 base dimensions')
            ui.table(columns=columns, rows=rows, row_key='name')


            ui.markdown('### Derived Dimensions')
            ui.markdown('Combining base dimensions together creates derived dimensions')
            dims = sorted(df_eqd['Base_quantity'].unique())
            with ui.expansion('Dimensions'):
                for d in dims:
                    ui.link(d, '/WikEq/Dimensions/'+d)
                    ui.markdown('')


@ui.page('/WikEq/Categories/{eq_cat}')
def WikEq(eq_cat):

    theme.add_header()
    with theme.row():
        theme.title(f"{eq_cat} Equations")

    with theme.row():
        # get all equations with blah
        eqns = df_eq.loc[df_eq['EQ_CAT']== eq_cat, 'Name'].sort_values()
        with ui.card():
            for e in eqns:
                ui.link(e, '/WikEq/Equations/'+e)







