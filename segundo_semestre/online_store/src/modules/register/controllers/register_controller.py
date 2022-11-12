# Nome: Caio B B G de Toledo
# RA: 20.01430-9

import streamlit as st
from src.modules.register.repositories.register_repository import RegisterRepository
from src.modules.login.models.user_model import UserModel


class RegisterController():
    def __init__(self) -> None:
        pass

    def register(self, name, email, pwd, verify_pwd, photo_url):
        if pwd != verify_pwd:
            st.session_state["registerError"] = 'Repita a mesma senha nos dois campos'
        else:
            new_user = UserModel(
                name=name,
                email=email,
                photo=photo_url,
                password=pwd
            )
            repo = RegisterRepository()
            if repo.register_user(new_user=new_user):
                st.session_state["isLogged"] = True
                st.session_state["showLoginError"] = False
            else:
                st.session_state["isLogged"] = False
                st.session_state["showLoginError"] = True
        return
