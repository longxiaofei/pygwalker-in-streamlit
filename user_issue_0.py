import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(layout="wide")
st.title("JSON to Pandas DataFrame and Visualization")

uploaded_file = st.file_uploader("Choose a JSON file", type="json")

if uploaded_file is not None:
    df = pd.read_json(uploaded_file)

    for col in df.select_dtypes(include=['datetime64[ns]', 'datetime64[ns, UTC]']).columns:
        df[col] = df[col].astype(str)

    pyg_app = StreamlitRenderer(df)

    pyg_app.explorer()
