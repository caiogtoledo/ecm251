# Nome: Caio B B G de Toledo
# RA: 20.01430-9

import streamlit as st
from modules.home.home_view import HomeView
from modules.login.controllers.login_controller import LoginController
from modules.register.controllers.register_controller import RegisterController
from modules.login.login_view import LoginView
from modules.car.car_controller import CarController
from modules.car.car_view import CarView
from modules.success.success_view import SuccessView
from modules.register.register_view import RegisterView

st.session_state["isLogged"] = False


class Main():
    def __init__(self) -> None:
        self.car_controller = CarController()
        if 'page' not in st.session_state:
            st.session_state['page'] = 'home'

        st.set_page_config(layout="wide")
        st.markdown("""
        <style>
            }}
                .reportview-container .main .block-container{{
                max-width: {percentage_width_main}%;
                padding-top: {1}rem;
                padding-right: {1}rem;
                padding-left: {1}rem;
                padding-bottom: {1}rem;
            }}

                .uploadedFile {{display: none}}
                footer {{visibility: hidden;}}
        </style>
        """, unsafe_allow_html=True)
        self.LoginController = LoginController()
        self.RegisterController = RegisterController()

    def runApp(self):
        if 'login' in st.session_state:
            if 'pwd' in st.session_state:
                self.LoginController.login(
                    st.session_state["login"], st.session_state["pwd"]
                )
        if not st.session_state["isLogged"]:
            if st.session_state['page'] == 'register':
                RegisterView(RegisterController=self.RegisterController)
            else:
                LoginView(LoginController=self.LoginController)
        else:
            if st.session_state['page'] == 'home':
                HomeView(car_controller=self.car_controller)
            elif st.session_state['page'] == 'car':
                CarView(car_controller=self.car_controller)
            elif st.session_state['page'] == 'success':
                SuccessView()
        # home_view.HomeView()


if __name__ == "__main__":
    Main().runApp()
