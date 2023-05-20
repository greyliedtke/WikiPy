"""
script to perform equation creation process...
"""
import theme
from nicegui import ui
from WikEq.DF.dfs import df_eq, df_eqv, df_eqd
from WikEq.equation_funcs import equation_v_detect


dims = ['Mass', 'Length', 'Time']


@ui.page('/WikEq/Create')
def WikEq():
    theme.add_header()

    def equation_input():
        eq_vars = equation_v_detect(eq_input.value)
        # check if name unique
        # show equation variables
        with theme.cc():
            ui.markdown(f"### Equation Variables")
            for e in eq_vars:
                ui.select(dims, label=f"{e} Dimension", value=dims[0])

    # with theme.row():
    with theme.cc():
        ui.markdown(f"### Equation Input")
        eq_input = ui.input("Equation Input")
        eq_name_input = ui.input("Equation Name")
        ui.button('Add Equation', on_click=lambda: equation_input())




# # solving equation
# solutions = symbol_solve(eq_input_1['eq'], var_key)

# # %%
# # get remaining information and verify parameters

# dim_inputs = [[psg.Text(e), psg.Combo(dims,default_value=dims[0], key=e)] for e in eq_vars]

# v_inputs = []
# for e in var_key:
#     dim_row = [
#         psg.Input(var_key[e][0], key=e+'_name'),
#         psg.Text(e),
#         psg.Input('desc', key=e+'_desc'),
#         psg.Input(var_key[e][1], key=e+'_dim'),
#         psg.Input(solutions[e], key=e+'_solved'), 
#         ]
#     v_inputs.append(dim_row)


# layout=[
#         v_inputs,
#         [psg.Input('link', key='link')],
#         [psg.Input('description', key='desc')],
#         [psg.Button('Done')]
#         ]

# win =psg.Window('EQ Category',layout)
# e, eq_p = win.read()
# win.close()

# # %%
# # write equation to db
# eq_args = [eq_input_1['eq_name'], eq_input_1['eq'], str(eq_vars), eq_p['desc'], eq_input_1['eq_cat'][0], eq_p['link']]
# q("INSERT INTO EQUATIONS (Name, Eqn, Variables, Short_Desc, EQ_CAT, WIKI_LINK) VALUES (?, ?, ?, ?, ?, ?)", args=eq_args)


# # %%
# # get eq id
# eq_id = q("SELECT EQ_id FROM EQUATIONS WHERE Name = ?", args=[eq_input_1['eq_name']])
# eq_id = eq_id[0][0]
# eq_id = int(eq_id)

# # %%
# # write all variables to db
# for v in var_key:
#     v_args = [eq_id, eq_p[v+'_name'], v, eq_p[v+'_dim'], eq_p[v+'_desc'], eq_p[v+'_solved']]
#     q("INSERT INTO EQ_VARS (EQ_id, D_name, Symbol, SI_units, Short_Desc, Solved) VALUES (?, ?, ?, ?, ?, ?)", args=v_args)




