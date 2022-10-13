# Nome: Caio B B G de Toledo
# RA: 20.01430-9

import streamlit as st


class LoginController():
    def __init__(self) -> None:
        pass

    def login(self, login, pwd):
        if login == 'caio' and pwd == 'senha':
            st.session_state["isLogged"] = True
        else:
            st.session_state["isLogged"] = False
        return
