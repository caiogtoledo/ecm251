# Nome: Caio B B G de Toledo
# RA: 20.01430-9

from src.dao.user_dao import UserDAO
from src.modules.login.models.user_model import UserModel
import streamlit as st


class RegisterRepository():
    login: str
    password: str
    user_on_db: UserModel

    def __init__(self) -> None:
        pass

    def register_user(self, new_user):
        try:
            UserDAO().add_user(new_user)
        except:
            st.session_state["registerError"] = 'Erro ao tentar cadastrar'
