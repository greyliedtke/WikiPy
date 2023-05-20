import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
from MerMaker.mermaid import render_mermaid, to_merm, new_node, new_relation


st.title('Mermaker')
node_input = st.text_input('Node Name')

if node_input:
    nodes = new_node(node_input)
    st.session_state[f"nodes"] = nodes
    nodes = nodes.split(',')
    cols = st.columns(3)
    with cols[0]:
        rels_from = st.selectbox('From', options=nodes, index=0)
    with cols[1]:
        rels_to = st.selectbox('To', options=nodes, index=len(nodes)-1)
    with cols[2]:
        rels_type = st.selectbox('Type', options=["dash", "arrow"])

    
relation_button = st.button("Add relation")

if relation_button:
    relations = new_relation([rels_from,rels_to,rels_type])
    st.session_state[f"relations"] = relations
    mt = to_merm(st.session_state[f"nodes"], st.session_state[f"relations"])
    render_mermaid(mt)
    print(st.session_state)
