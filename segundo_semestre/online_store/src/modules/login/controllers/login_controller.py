# Nome: Caio B B G de Toledo
# RA: 20.01430-9

import streamlit as st
from src.modules.login.repositories.login_repository import LoginRepository


class LoginController():
    def __init__(self) -> None:
        pass

    def login(self, login, pwd):
        repo = LoginRepository()
        if repo.check_login(login=login, password=pwd):
            st.session_state["isLogged"] = True
            st.session_state["showLoginError"] = False
        else:
            st.session_state["isLogged"] = False
            st.session_state["showLoginError"] = True
        return
