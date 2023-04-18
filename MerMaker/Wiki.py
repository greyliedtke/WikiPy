from nicegui import ui, app
import json
import theme
import pandas as pd
# import uuid
# from starlette.middleware.sessions import SessionMiddleware
# from starlette.requests import Request


# def render_mermaid(merm_c):
#     merm_j = json.loads(merm_c.content)
#     nodes = merm_j['nodes']
#     relations = merm_j['relations']

#     # update nodes
#     # select_to.options = nodes
#     # select_to.value = nodes[0]
#     # select_to.update()
#     # select_from.options = nodes
#     # select_from.value = nodes[-1]
#     # select_from.update()

#     node_txt = ''
#     # node_container.clear()
#     for n in nodes: 
#         node_txt+= f"- {n}\n"
#         # with node_container:
#         #     ui.button(f"x: {n}", on_click=lambda: clear_node(n))
#     # md_nodes.content = node_txt

#     # update relations
#     relations_txt = ''
#     for r in relations: 
#         relations_txt+= f"- {r[0]}{r[2]}{r[1]}\n"
#     # md_relations.content = relations_txt

#     # render mermaid content
#     merm_txt = """%% Mermaid Diagram\ngraph TD;\n\n"""
#     merm_txt+= f"%% Nodes\n"
#     for n in nodes: 
#         merm_txt+= f"{n}\n"
#     merm_txt+= f"\n%% Relations\n"
#     for r in relations: 
#         merm_txt+= f"{r[0]}-->{r[1]}\n"

#     # ta_mermaid.value = merm_txt
#     # merm_c.content = merm_txt


# def new_node(merm_c, node_name, node_container, ndf):
#     merm_j = json.loads(merm_c.content)
#     nodes = merm_j['nodes']
#     relations = merm_j['relations']
#     current_nodes = ndf.options
#     print(current_nodes)
#     session = Request.session
#     session['mermaid_content'] = {'Nodes': ['greyses'], 'Relations': ['greymans']}
#     ndff = pd.DataFrame(data={'Nodes': ['ex'], 'Desc':['desc']})
#     new_row = [node_name, node_name]
#     new_row = pd.DataFrame({'Nodes': [node_name], 'Desc': [node_name]})
#     ndff = pd.concat([ndff, new_row], ignore_index=True)
#     node_container.clear
#     ndf = ui.aggrid.from_pandas(ndff)
    
#     # rowd = current_nodes['rowData']
#     # rowd.append([node_name, node_name])
#     # ndf.options['rowData'].append(['grey', 90])
#     ndf.update()


#     if node_name in nodes:
#         print('duplicate node')
#         pass
#     else:
#         nodes.append(node_name)
#         merm_c.content = json.dumps({'nodes':nodes, 'relations':relations})
#         render_mermaid(merm_c)
#         node_txt = ''
#         node_container.clear()
#         for n in nodes: 
#             node_txt+= f"- {n}\n"
#             with node_container:
#                 ui.button(f"x: {n}", on_click=lambda: clear_node(n))


# def new_relation(merm_c, node_container, n_from, n_to, r_type):
#     if r_type == 'Dashed': cnxn = ' --- '
#     elif r_type == 'Arrow': cnxn = ' --> '
#     else: cnxn = ' --> '
#     merm_j = json.loads(merm_c.content)
#     relations = merm_j['relations']
#     relations.append([n_from, n_to, cnxn])
#     render_mermaid(merm_c.content)

# def clear_all(nodes, relations):
#     nodes.clear()
#     relations.clear()
#     new_node(nodes, '')
#     pass

# def clear_node(nodes, del_node):
#     print('del', del_node)
#     nodes.remove(del_node)
#     render_mermaid('')

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
    
    nodes = ['example']
    relations = [['example', 'example', 'example']]

    with theme.row():
        with theme.cc():
            ui.markdown("### Nodes")
            node_container = ui.card()
            with node_container:
                ns = ui.aggrid({
                        'columnDefs': [
                        {'headerName': 'Name', 'field': 'name', 'checkboxSelection': True}],
                        "rowData": [0],
                        'rowSelection': 'single',
                    })

            

            def new_noder(new_node):
                nodes.append(new_node)
                node_container.clear()
                with node_container:
                    dff = pd.DataFrame(data={'Nodes': nodes})
                    ui.markdown(str(nodes))
                    rd = [{"name": n} for n in nodes]
                    ns = ui.aggrid({
                        'columnDefs': [
                        {'headerName': 'Name', 'field': 'name', 'checkboxSelection': True}],
                        "rowData": rd,
                        'rowSelection': 'single',
                    })

                rel_from.options = nodes
                rel_from.update()
                rel_to.options = nodes
                rel_to.value = nodes[-1] 
                rel_to.update()
                update_mermaid()

            async def del_node():
                nd = await ns.get_selected_rows()
                print(nd)
                    
            node_input = ui.input('Node')
            ui.button('Add Node', on_click=lambda: new_noder(node_input.value))
            ui.button('Delete Node', on_click=lambda: del_node)
            
        
        with theme.cc():
            ui.markdown("### Relations")
            rel_container = ui.card()
            def new_rel(new_rel):
                relations.append(new_rel)
                rel_container.clear()
                with rel_container:
                    dff = pd.DataFrame(data={'Relations': relations})
                    ui.markdown(str(nodes))
                    ui.aggrid.from_pandas(dff)
                update_mermaid()
                    
            with ui.row():
                line_types = ["---", "-->"]
                rel_input = ui.select(line_types, value=line_types[0])
                rel_from = ui.select(nodes, value=nodes[0])
                rel_to = ui.select(nodes, value=nodes[0])

            ui.button('Add Relation', on_click=lambda: new_rel([rel_from.value, rel_to.value, rel_input.value]))

    with theme.cc():
        ui.markdown("### Mermaid")
        mermaid_container = ui.card()
        
        def update_mermaid():
            merm_blob = render_mermaid(nodes, relations)
            mermaid_container.clear()
            with mermaid_container:
                ui.textarea("Mermaid Code", value=merm_blob)
                ui.mermaid(merm_blob)
