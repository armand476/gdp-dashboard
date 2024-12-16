import streamlit as st
import pandas as pd
import numpy as np
st.markdown(
    """
    <div style="text-align: center; color:#00561b; font-size: 50px; font-weight: bold;">
        Mon application
    </div>
    """,
    unsafe_allow_html=True
)
température = st.number_input("Température :", min_value=35.0, max_value=45.0, step=0.1)
age = st.selectbox(
        "Age", 
        options=np.arange(0, 130, 1).tolist()
    )
sat = st.selectbox(
        "Saturation en oxygéne", 
        options=np.arange(60, 100, 0.1).tolist()
    )
cols=st.columns(2)
with cols[0]:
    t1 = st.selectbox(
        "Tension systollique", 
        options=np.arange(10, 200, 1)
    )
with cols[1]:
        
    t2 = st.selectbox(
        "Tension diastollique", 
        options=np.arange(10, 200, 1)
    )
