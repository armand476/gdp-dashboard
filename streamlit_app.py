import streamlit as st
import pandas as pd
import math
from pathlib import Path

st.markdown(
    """
    <div style="text-align: center; color:#00561b; font-size: 50px; font-weight: bold;">
        Mon application
    </div>
    """,
    unsafe_allow_html=True
)
température = st.selectbox(
        "Température", 
        options=list(range(
    )
age = st.selectbox(
        "Age", 
        options=list(range(
    )
sat = st.selectbox(
        "Saturation en oxygéne", 
        options=list(range(
    )
cols=st.columns(2)
with cols[0]:
    t1 = st.selectbox(
        "Tension systollique", 
        options=list(range(
    )
with cols[1]:
        
    t2 = st.selectbox(
        "Tension diastollique", 
        options=list(range(
    )
