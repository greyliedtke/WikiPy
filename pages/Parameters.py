import streamlit as st

pp = st.experimental_get_query_params()
st.write(pp)
st.write("https://example.com/my-page?param1=value1&param2=value2&param3=value3")
{"show_map": ["True"], "selected": ["asia", "america"]}