"""
script to generate mermaid content
"""

# make mermaid diagrams
import streamlit.components.v1 as components
import streamlit as st



# handling session 
def new_relation(new_rels):
    """
    for every new nodes... add it to session
    """

    if "relations" in st.session_state:
        rel_txt = st.session_state["relations"]
        rel_txt+=f";{new_rels}"
    else:
        rel_txt = f"{new_rels}"
    return rel_txt

def new_node(nn):
    """
    for every new nodes... add it to session
    """

    if "nodes" in st.session_state:
        node_txt = st.session_state["nodes"]
        nodes = node_txt.split(",")
        if nn not in nodes:
            node_txt+=f",{nn}"
    else:
        node_txt = f"{nn}"

    return node_txt




def to_merm(nodes, relations):
    """
    function to turn all nodes and relations into mermaid text
    """

    nodes = nodes.split(",")
    relations = relations.split(";")

    # render mermaid content
    merm_txt = """%% Mermaid Diagram\ngraph TD;\n\n"""
    merm_txt+= f"%% Nodes\n"
    for n in nodes: 
        merm_txt+= f"{n}\n"
    merm_txt+= f"\n%% Relations\n"
    print(relations)
    for r in relations: 
        # r = r
        r = r[1:-1].split(",")
        merm_txt+= f"{r[0][1:-1]}-->{r[1][2:-1]}\n"
    
    print(merm_txt)
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