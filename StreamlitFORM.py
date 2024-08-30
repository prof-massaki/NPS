import streamlit as st
import webbrowser
from io import BytesIO
import requests
import pandas as pd

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

from urllib.request import urlopen

def SendMAIL(assunto):
    # create message object instance 
    msg = MIMEMultipart()     
    # setup the parameters of the message 
    password = "makchgxvssjzogky"
    msg['From'] = "prof.massaki@gmail.com"
    msg['To'] =   "actspsolucoesparapessoas+cgaew9i3s6kcacagaoeg@boards.trello.com"
    msg['Subject'] = assunto
    #file = "Python.pdf"
    # attach image to message body 
    #msg.attach(MIMEText(open(file).read()))     
    # create server 
    server = smtplib.SMTP('smtp.gmail.com: 465')     
    server.starttls()     
    # Login Credentials for sending the mail 
    server.login(msg['From'], password)      
    # send the message via the server. 
    server.sendmail(msg['From'], msg['To'], msg.as_string("MENSAGEM TESTE"))     
    server.quit()

st.set_page_config(
     page_title="Formulário de Cadastro",
     page_icon=":date:",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'mailto:informacoes.actsp@gmail.com',
         'Report a bug': "mailto:informacoes.actsp@gmail.com",
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

