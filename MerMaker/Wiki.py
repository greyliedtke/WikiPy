from nicegui import ui
import json
import theme
import pandas as pd

def render_mermaid(merm_c):
    merm_j = json.loads(merm_c.content)
    nodes = merm_j['nodes']
    relations = merm_j['relations']

    # update nodes
    # select_to.options = nodes
    # select_to.value = nodes[0]
    # select_to.update()
    # select_from.options = nodes
    # select_from.value = nodes[-1]
    # select_from.update()

    node_txt = ''
    # node_container.clear()
    for n in nodes: 
        node_txt+= f"- {n}\n"
        # with node_container:
        #     ui.button(f"x: {n}", on_click=lambda: clear_node(n))
    # md_nodes.content = node_txt

    # update relations
    relations_txt = ''
    for r in relations: 
        relations_txt+= f"- {r[0]}{r[2]}{r[1]}\n"
    # md_relations.content = relations_txt

    # render mermaid content
    merm_txt = """%% Mermaid Diagram\ngraph TD;\n\n"""
    merm_txt+= f"%% Nodes\n"
    for n in nodes: 
        merm_txt+= f"{n}\n"
    merm_txt+= f"\n%% Relations\n"
    for r in relations: 
        merm_txt+= f"{r[0]}-->{r[1]}\n"

    # ta_mermaid.value = merm_txt
    # merm_c.content = merm_txt


def new_node(merm_c, node_name, node_container, ndf):
    merm_j = json.loads(merm_c.content)
    nodes = merm_j['nodes']
    relations = merm_j['relations']
    current_nodes = ndf.options
    print(current_nodes)
    ndff = pd.DataFrame(data={'Nodes': ['ex'], 'Desc':['desc']})
    new_row = [node_name, node_name]
    new_row = pd.DataFrame({'Nodes': [node_name], 'Desc': [node_name]})
    ndff = pd.concat([ndff, new_row], ignore_index=True)
    node_container.clear
    ndf = ui.aggrid.from_pandas(ndff)
    
    # rowd = current_nodes['rowData']
    # rowd.append([node_name, node_name])
    # ndf.options['rowData'].append(['grey', 90])
    ndf.update()


    if node_name in nodes:
        print('duplicate node')
        pass
    else:
        nodes.append(node_name)
        merm_c.content = json.dumps({'nodes':nodes, 'relations':relations})
        render_mermaid(merm_c)
        node_txt = ''
        node_container.clear()
        for n in nodes: 
            node_txt+= f"- {n}\n"
            with node_container:
                ui.button(f"x: {n}", on_click=lambda: clear_node(n))


def new_relation(merm_c, node_container, n_from, n_to, r_type):
    if r_type == 'Dashed': cnxn = ' --- '
    elif r_type == 'Arrow': cnxn = ' --> '
    else: cnxn = ' --> '
    merm_j = json.loads(merm_c.content)
    relations = merm_j['relations']
    relations.append([n_from, n_to, cnxn])
    render_mermaid(merm_c.content)

def clear_all(nodes, relations):
    nodes.clear()
    relations.clear()
    new_node(nodes, '')
    pass

def clear_node(nodes, del_node):
    print('del', del_node)
    nodes.remove(del_node)
    render_mermaid('')

# ---------------------------------------------------


# UI
@ui.page("/MerMaker")
def page():
    theme.add_header()
    

    nodes = ['OCC', 'Generator', 'load']
    relations = [['OCC', 'load', '---']]

    merm = {'nodes': nodes, 'relations': relations}
    merm_c = ui.markdown(json.dumps(merm))

    with theme.row():
        with theme.cc():
            ui.markdown("### Nodes")
            md_nodes = ui.markdown('- Nodes')
            node_container = ui.column()
            with node_container:
                dff = pd.DataFrame(data={'Nodes': ['ex'], 'Desc':['desc']})
                ndf = ui.aggrid.from_pandas(dff)
            node_input = ui.input('Node')
            ui.button('Add Node', on_click=lambda: new_node(merm_c, node_input.value, node_container, ndf))

    with theme.row():
        with theme.cc():
            ui.markdown("### Node Input")

        # with theme.cc():
        #     ui.markdown("### Relation Input")

            # with ui.row():
            #     select_from = ui.select([])
            #     select_to = ui.select([])
            #     select_type = ui.select(['Dash', 'Arrow'])
                # ui.button('Add Relation', on_click=lambda: new_relation(merm_c.content, select_from.value, select_to.value, select_type.value))
        with theme.cc():
            ui.markdown("### Diagram Control")
            with ui.row():
                ui.button('Clear', on_click=lambda: clear_all())


    


        with theme.cc():
            ui.markdown("### Relations")
            md_relations = ui.markdown('- Relations')

        with theme.cc():
            ui.markdown("### Mermaid Output")
            ta_mermaid = ui.textarea(label='Code', value=f"")
            mm_mermaid = ui.mermaid(f"")
