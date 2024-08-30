import streamlit as st
import webbrowser
from io import BytesIO
import requests
import pandas as pd

st.set_page_config(
     page_title="Formulário de Cadastro",
     page_icon=":date:",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'mailto:prof.massaki@gmail.com',
         'Report a bug': "mailto:prof.massaki@gmail.com",
         'About': "#### Desenvolvedor: Massaki de O. Igarashi"
     }
 )

new=2

#st.write(df.head())
st.title('Cadastr0')
st.subheader('Entraremos em contato com você em breve!')

txtNome = st.text_input("Digite seu nome completo 👇")
if txtNome:
    url= 'https://docs.google.com/forms/d/e/1FAIpQLSe3k4qby8XCLb4ABrZ972PW_VK4PS3aJo_qCEX-nfDsYiaMeg/formResponse?&submit=Submit?usp=pp_url&entry.705323696=' + str(txtNome)

if st.button('Confirmar 👇'):
    
    response = urlopen(f'{url}')
    html = response.read()

