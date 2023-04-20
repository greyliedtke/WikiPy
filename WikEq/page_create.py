"""
script to perform equation creation process...
"""
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


# %% [markdown]
# # Creating an equation for wikeq.com

# %%
# imports
from DB.DB_Connect import q
import PySimpleGUI as psg

from EQ.EQ_Create.EQ_Funcs import detect_vars, symbol_solve


# %%
eq_cats = q("SELECT DISTINCT EQ_CAT FROM EQUATIONS")
layout=[
        [psg.Combo(eq_cats,default_value=eq_cats[0], key='eq_cat')],
        [psg.Input('Equation Name', key='eq_name')],
        [psg.Input('Equation', key='eq')],
        [psg.Button('Done')]
        ]

win =psg.Window('EQ Category',layout)
e, eq_input_1 = win.read()
win.close()


# %%
# validate name unique and parse equation
eq_name_unique = q("SELECT Name FROM EQUATIONS WHERE Name = ?", args=[eq_input_1['eq_name']])
eq_unique = q("SELECT Name FROM EQUATIONS WHERE Eqn = ?", args=[eq_input_1['eq']])

if max(len(eq_unique), len(eq_name_unique)) > 0:
    print('exists...')

else:
    # parse through variables and solve....
    eq_vars = detect_vars(eq_input_1['eq'])
    



# %%
# present dropdown options for variables

dims = q("SELECT Base_quantity, SI_base_unit FROM DERIVED_DIMENSIONS")
dim_inputs = [[psg.Text(e), psg.Combo(dims,default_value=dims[0], key=e)] for e in eq_vars]

layout=[
        dim_inputs,
        [psg.Button('Done')]
        ]

win = psg.Window('EQ Category',layout)
e, var_key = win.read()
win.close()

# %%
# solving equation
solutions = symbol_solve(eq_input_1['eq'], var_key)

# %%
# get remaining information and verify parameters

dim_inputs = [[psg.Text(e), psg.Combo(dims,default_value=dims[0], key=e)] for e in eq_vars]

v_inputs = []
for e in var_key:
    dim_row = [
        psg.Input(var_key[e][0], key=e+'_name'),
        psg.Text(e),
        psg.Input('desc', key=e+'_desc'),
        psg.Input(var_key[e][1], key=e+'_dim'),
        psg.Input(solutions[e], key=e+'_solved'), 
        ]
    v_inputs.append(dim_row)


layout=[
        v_inputs,
        [psg.Input('link', key='link')],
        [psg.Input('description', key='desc')],
        [psg.Button('Done')]
        ]

win =psg.Window('EQ Category',layout)
e, eq_p = win.read()
win.close()

# %%
# write equation to db
eq_args = [eq_input_1['eq_name'], eq_input_1['eq'], str(eq_vars), eq_p['desc'], eq_input_1['eq_cat'][0], eq_p['link']]
q("INSERT INTO EQUATIONS (Name, Eqn, Variables, Short_Desc, EQ_CAT, WIKI_LINK) VALUES (?, ?, ?, ?, ?, ?)", args=eq_args)


# %%
# get eq id
eq_id = q("SELECT EQ_id FROM EQUATIONS WHERE Name = ?", args=[eq_input_1['eq_name']])
eq_id = eq_id[0][0]
eq_id = int(eq_id)

# %%
# write all variables to db
for v in var_key:
    v_args = [eq_id, eq_p[v+'_name'], v, eq_p[v+'_dim'], eq_p[v+'_desc'], eq_p[v+'_solved']]
    q("INSERT INTO EQ_VARS (EQ_id, D_name, Symbol, SI_units, Short_Desc, Solved) VALUES (?, ?, ?, ?, ?, ?)", args=v_args)

