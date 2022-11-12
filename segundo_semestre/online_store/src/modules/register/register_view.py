# Nome: Caio B B G de Toledo
# RA: 20.01430-9

import streamlit as st


class RegisterView():
    def __init__(self, RegisterController) -> None:
        st.title('Cadastro')
        if 'registerError' in st.session_state and st.session_state['registerError'] != '':
            st.write(st.session_state['registerError'])
        self.name = st.text_input(label='Nome completo')
        self.email = st.text_input(label='email')
        self.pwd = st.text_input(label='Senha', type="password")
        self.verify_pwd = st.text_input(
            label='Repita Sua Senha', type="password")
        self.photoUrl = st.text_input(label='URL de foto')
        st.session_state["name"] = self.name
        st.session_state["email"] = self.email
        st.session_state["photoUrl"] = self.photoUrl
        st.session_state["pwd"] = self.pwd
        if 'email' in st.session_state:
            if 'photoUrl' in st.session_state:
                if 'name' in st.session_state:
                    if 'pwd' in st.session_state:
                        st.button(
                            "Cadastrar",
                            on_click=RegisterController.register,
                            kwargs={
                                "name": self.name,
                                "email": self.email,
                                "pwd": self.pwd,
                                "verify_pwd": self.verify_pwd,
                                "photo_url": self.photoUrl
                            }
                        )
        st.button('Já tenho cadastro', on_click=self.openLogin)

    def openLogin(self):
        st.session_state['page'] = 'login'
