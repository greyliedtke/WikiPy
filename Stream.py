import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components

# Define the Mermaid diagram
diagram = """
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
"""


def mermaid(code: str) -> None:
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


mermaid(
    """
    graph LR
        A --> B --> C
        m + b
    """
)

print("fuck")



st.title('GreyWeb')
mermaid(
    """
    graph LR
        A --> B --> C
    """
)

st.header("Do things here")

