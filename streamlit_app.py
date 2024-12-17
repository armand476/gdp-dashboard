import streamlit as st
import pandas as pd
import numpy as np
import json
import re
import requests
import os
from openai import OpenAI
image_url = "https://github.com/armand476/gdp-dashboard/blob/main/Download%20Doctor%20Johnny%20Sins%20Wallpaper%20_%20Wallpapers_com.jpg?raw=true"
if not 'question' in st.session_state:
    st.session_state['question']=[]
    st.session_state['réponse']=[]
if st.button("Réinitialisez conversation"):
    st.session_state['question']=[]
    st.session_state['réponse']=[]
# Configurer la clé API comme variable d'environnement
os.environ["XAI_API_KEY"] = "xai-gZAc0yZ9WhUSWPIlxkdgLDWLor2O2I1xpN48yGFM9QOWrKrilgBFlA8OFXTWJ8UzsGu1JdV1cuQPBccQ"

# Initialiser le client avec la clé API
client = OpenAI(
    api_key=os.environ["XAI_API_KEY"],
    base_url="https://api.x.ai/v1",
)

# Faire une requête à l'API Grok




st.markdown(
    f"""
    <style>
    div.stApp {{
        background-image: url({image_url});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
liste_mesure=["IMC","Taille","Poids"]
step=[1,1,1]
min=[5,5,1]
max=[50,300,400]

st.markdown(
    """
    <div style="text-align: center; color:#00561b; font-size: 50px; font-weight: bold;">
        MEDICIA
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
colage=st.columns(2)
with colage[0]:
    age =  st.number_input("Age :", min_value=0, max_value=150, step=1)
with colage[1]:
    typeage = st.selectbox(
        "Unité age", 
        options=["ans", "mois"], 
        key="unité_age"
    )
température = st.number_input("Température :", min_value=35.0, max_value=45.0, step=0.1)
sat = st.number_input("Saturation d'oxygéne :", min_value=0.0, max_value=100.0, step=0.1)
cols=st.columns(2)
with cols[0]:
    t1 = st.number_input("Tension systollique :", min_value=0, max_value=300, step=1)
with cols[1]:
    t2 = st.number_input("Tension diastollique :", min_value=0, max_value=300, step=1)   
st.markdown("<hr style='border:1px solid black;'>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center;text-decoration:underline;font-size:20px;">
       Mesures Réalisées :
    </div>
    """,
    unsafe_allow_html=True
)
n=len(liste_mesure)
#st.session_state['mesure']= [False] * n
v= [False] * n
r= [None] * n
colmesure=st.columns(n)
for i in range(n):
    with colmesure[i]:
        v[i] = st.checkbox(liste_mesure[i],v[i])
for i in range(n):
    if v[i]== True :
        r[i] = st.number_input(liste_mesure[i], min_value=min[i], max_value=max[i], step=step[i])
        
        
    
autres_mesures= st.text_input("Autres mesures :")
st.markdown("<hr style='border:1px solid black;'>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center;text-decoration:underline;font-size:20px;">
        Description plus profonde :
    </div>
    """,
    unsafe_allow_html=True
)
symptome= st.text_input("Décrivez les symptomes du patient :")
antécédents= st.text_input("Le patient a-t-il des traitements si oui lesquels ?")
st.write(st.session_state['question'])
for i in range(len(st.session_state['question'])):
    st.session_state['réponse'][i]= st.text_input(st.session_state['question'][i])

if st.button("Envoyez"):
    st.write("envoyez")
    texte="Tu mettras entre guillement toute les questions que tu as"
    '''completion = client.chat.completions.create(
    model="grok-beta",
    messages=[
        {"role": "system", "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."},
        {"role": "user", "content": "Explain the risks of improper AI usage and its contribution to autocratic regimes."},
    ],
)    '''
    #st.write(completion.choices[0].message.content)
    response='Voici "la première phrase", puis "la seconde phrase", et enfin "une dernière phrase".'
    l= re.findall(r'"(.*?)"', response)
    st.session_state['question']=st.session_state['question']+l
    st.write(st.session_state['question'])
    if (len(st.session_state['question'])>len(st.session_state['réponse'])):
        for i in range((len(st.session_state['question'])-len(st.session_state['réponse']))):
            st.session_state['réponse'].append("")
    
   
