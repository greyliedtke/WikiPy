import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components

# Define the Mermaid diagram
mm_nodes = ['Node']
st.session_state['mm_nodes'] = []
mm_rels = [['Node', 'Node', 'Node']]

def new_node(nn):
    st.session_state[f"n_{nn}"] = mm_nodes  # Dictionary like API
    nodes = []
    for m in st.session_state:
        if "n_" in m:
            nodes.append(m)
    return nodes


def to_merm(nodes, relations):
    """
    function to turn all nodes and relations into mermaid text
    """

    node_txt = ''
    for n in nodes: 
        node_txt+= f"- {n}\n"

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


def render_mermaid(code: str) -> None:
    components.html(
        f"""
        <pre class="mermaid">
            {code}
        </pre>

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """
    )

st.title('Mermaker')
node_input = st.text_input('Node Name')

rels_from = st.selectbox('From', ['from', 'to', "---"])
rels_to = st.selectbox('To', ['from', 'to', "---"])
rels_type = st.selectbox('Type', ['from', 'to', "---"])

relation_button = st.button("Add relation")
mt = to_merm(mm_nodes, mm_rels)
render_mermaid(mt)

if node_input:
    mm_nodes = new_node(node_input)
    print(mm_nodes)
    mt = to_merm(mm_nodes, mm_rels)
    render_mermaid(mt)

if relation_button:
    mm_rels.append([rels_from, rels_to, rels_type])
    mt = to_merm(mm_nodes, mm_rels)
    render_mermaid(mt)


st.write(st.session_state)
query_params = st.experimental_get_query_params()
st.write(query_params)