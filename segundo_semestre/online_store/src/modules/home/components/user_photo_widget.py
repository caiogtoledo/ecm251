# Nome: Caio B B G de Toledo
# RA: 20.01430-9

import streamlit as st


def UserPhotoWidget(url):
    if url == '':
        url = 'https://static.vecteezy.com/ti/vetor-gratis/p1/1840618-imagem-perfil-icone-masculino-icone-humano-ou-pessoa-sinal-e-simbolo-gr%C3%A1tis-vetor.jpg'
    st.markdown(
        f"""
        <img 
            src="{url}"
            style="width: 100px; border-radius:50px"
        />
        """,
        unsafe_allow_html=True
    )
