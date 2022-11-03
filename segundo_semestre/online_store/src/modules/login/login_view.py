# Nome: Caio B B G de Toledo
# RA: 20.01430-9

import streamlit as st


class LoginView():
    def __init__(self, LoginController) -> None:
        self.login = st.text_input(label='Login')
        self.pwd = st.text_input(label='Senha', type="password")
        st.session_state["login"] = self.login
        st.session_state["pwd"] = self.pwd
        st.button(
            "Login",
            on_click=LoginController.login,
            kwargs={
                "login": self.login,
                "pwd": self.pwd
            }
        )
