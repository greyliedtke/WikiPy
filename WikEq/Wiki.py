from nicegui import ui
from WikEq.DF.dfs import df_eq, df_eqv, df_eqd
import theme
from nicegui import Tailwind, ui
import WikEq.page_equations, WikEq.page_dimensions

bd = ['Length', 'Mass', 'Time', 'Electric Current', 'Temperature', 'Moles', 'Luminosity']




@ui.page("/WikEq")
def WikEq():
    theme.add_header()
    with theme.row():
        theme.title("*WikEQ*")
        theme.subtitle("A symbolic solving and dimension referencing equation wiki.")

    with theme.row():
        with theme.cc():
            ui.markdown("### Equation Categories")
            # get unique equation categories
            eq_cats = sorted(df_eq["EQ_CAT"].unique())
            for e in eq_cats:
                ui.link(e, "/WikEq/Categories/" + e)
        with theme.cc():
            ui.markdown("### Example Equations")
            # 3 random equations
            eqns = df_eq.sample(n=3)
            eqns = eqns[["Name", "Eqn"]].sort_values(by="Name")
            with ui.card():
                for i,row in eqns.iterrows():
                    with ui.row():
                        ui.markdown(f"**[{row['Name']}](/WikEq/Equations/{row['Name']})**: <em>{row['Eqn']}</em>")

    with theme.row():
        with theme.cc():
            ui.markdown("### Base Dimensions")
            ui.markdown("All dimensions originate from the 7 [base dimensions](https://en.wikipedia.org/wiki/List_of_physical_quantities)")
            for d in bd:
                ui.markdown(f"**[{d}](/WikEq/Dimensions/{d})**")

        with theme.cc():
            ui.markdown("### Derived Dimensions")
            ui.markdown("Combining base dimensions together creates [derived dimensions](https://en.wikipedia.org/wiki/List_of_physical_quantities)")
            dims = sorted(df_eqd["Base_quantity"].unique())
            with ui.expansion("Dimensions"):
                for d in dims:
                    ui.link(d, "/WikEq/Dimensions/" + d)
                    ui.markdown("")

@ui.page("/WikEq/Categories/{eq_cat}")
def WikEq(eq_cat):
    theme.add_header()

    with theme.cc():
        # get all equations with blah
        ui.markdown(f"{eq_cat} Equations")

        eqns = df_eq.loc[df_eq["EQ_CAT"] == eq_cat]
        eqns = eqns[["Name", "Eqn"]].sort_values(by="Name")
        for i,row in eqns.iterrows():
            ui.markdown(f"**[{row['Name']}](/WikEq/Equations/{row['Name']})**: <em>{row['Eqn']}</em>")
