# Nome: Caio B B G de Toledo
# RA: 20.01430-9

import streamlit as st


class LoginView():
    def __init__(self, LoginController) -> None:
        st.title('Login')
        if "loginError" in st.session_state:
            if st.session_state["loginError"] != '' and len(st.session_state['pwd']) > 0:
                st.write(st.session_state["loginError"])
        self.login = st.text_input(label='Login')
        self.pwd = st.text_input(label='Senha', type="password")
        st.session_state["login"] = self.login
        st.session_state["pwd"] = self.pwd
        if 'login' in st.session_state and 'pwd' in st.session_state:
            st.button(
                "Login",
                on_click=LoginController.login,
                kwargs={
                    "login": self.login,
                    "pwd": self.pwd
                }
            )
        st.button('Não tenho cadastro', on_click=self.openRegister)

    def openRegister(self):
        st.session_state['page'] = 'register'
