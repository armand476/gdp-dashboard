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
st.markdown("<hr style='border:1px solid black;'>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center;text-decoration:underline;font-size:20px;">
        Bilan :
    </div>
    """,
    unsafe_allow_html=True
)
age =  st.number_input("Age :", min_value=0, max_value=1, step=1)
température = st.number_input("Température :", min_value=35.0, max_value=45.0, step=0.1)
sat = st.number_input("Saturation d'oxygéne :", min_value=0.0, max_value=100.0, step=0.1)
cols=st.columns(2)
with cols[0]:
    t1 = st.number_input("Tension systollique :", min_value=0, max_value=300, step=1)
with cols[1]:
    t2 = st.number_input("Tension systollique :", min_value=0, max_value=300, step=1)   
st.markdown("<hr style='border:1px solid black;'>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center;text-decoration:underline;font-size:20px;">
        Description symptome :
    </div>
    """,
    unsafe_allow_html=True
)
symptome= st.text_input("Symptome :")
antécédents= st.text_input("Symptome :")
   
