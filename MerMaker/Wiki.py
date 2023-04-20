from nicegui import ui, app
import json
import theme
import pandas as pd
import asyncio

# ---------------------------------------------------
def render_mermaid(nodes, relations):
    node_txt = ''
    # node_container.clear()
    for n in nodes: 
        node_txt+= f"- {n}\n"

    # update relations
    relations_txt = ''
    for r in relations: 
        relations_txt+= f"- {r[0]}{r[2]}{r[1]}\n"

    # render mermaid content
    merm_txt = """%% Mermaid Diagram\ngraph TD;\n\n"""
    merm_txt+= f"%% Nodes\n"
    for n in nodes: 
        merm_txt+= f"{n}\n"
    merm_txt+= f"\n%% Relations\n"
    for r in relations: 
        merm_txt+= f"{r[0]}-->{r[1]}\n"
    
    return merm_txt



# UI
@ui.page("/MerMaker")
def page():

    theme.add_header()
    
    nodes = []
    relations = []

    with theme.row():
        with theme.cc():
            ui.markdown("### Nodes")
            # node_container = ui.card()
            # with node_container:
            #     ns = ui.aggrid({
            #             'columnDefs': [
            #             {'headerName': 'Name', 'field': 'name', 'checkboxSelection': True}],
            #             "rowData": [0],
            #             'rowSelection': 'single',
            #         })

            

            def new_noder(new_node):
                nodes.append(new_node)
                # node_container.clear()
                # with node_container:
                    # dff = pd.DataFrame(data={'Nodes': nodes})
                    # ui.markdown(str(nodes))
                    # rd = [{"name": n} for n in nodes]
                    # ns = ui.aggrid({
                    #     'columnDefs': [
                    #     {'headerName': 'Name', 'field': 'name', 'checkboxSelection': True}],
                    #     "rowData": rd,
                    #     'rowSelection': 'single',
                    # })

                rel_from.options = nodes
                rel_from.value = nodes[0]
                rel_from.update()
                rel_to.options = nodes
                rel_to.value = nodes[-1] 
                rel_to.update()
                update_mermaid()

                    
            node_input = ui.input('Node')
            ui.button('Add Node', on_click=lambda: new_noder(node_input.value))

        with theme.cc():
            ui.markdown("### Relations")
            # rel_container = ui.card()
            def new_rel(new_rel):
                relations.append(new_rel)
                # rel_container.clear()
                # with rel_container:
                #     dff = pd.DataFrame(data={'Relations': relations})
                #     ui.markdown(str(nodes))
                #     ui.aggrid.from_pandas(dff)
                update_mermaid()
                    
            with ui.row():
                line_types = ["---", "-->"]
                rel_input = ui.select(line_types, value=line_types[0])
                rel_from = ui.select(nodes)
                rel_to = ui.select(nodes)

            ui.button('Add Relation', on_click=lambda: new_rel([rel_from.value, rel_to.value, rel_input.value]))

    with theme.cc():
        ui.markdown("### Mermaid")
        with ui.row():
            ui.button('Update')
            ui.button('Copy')
        mermaid_container = ui.card().classes("w-600")
        
        def update_mermaid():
            merm_blob = render_mermaid(nodes, relations)
            mermaid_container.clear()
            with mermaid_container:
                with ui.row():
                    ui.textarea("Mermaid Code", value=merm_blob).classes('w-600 h-150')
                    ui.mermaid(merm_blob)
        update_mermaid()
