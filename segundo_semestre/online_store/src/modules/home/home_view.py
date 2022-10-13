from asyncore import write
import streamlit as st

from src.modules.home.components.product_widget import ProductWidget
from src.modules.home.components.user_photo_widget import UserPhotoWidget
from src.modules.home.repositories.products_repository import ProductsRepository
import streamlit_nested_layout
from src.modules.car.car_controller import CarController


class HomeView():
    def __init__(self, car_controller: CarController) -> None:
        col1_header, col4_header, col2_header, col5_header, col3_header = st.columns([
                                                                                     1, 1, 2, 1, 1])
        repo = ProductsRepository()

        with col1_header:
            st.image("../assets/logo.png", width=100)

        with col2_header:
            SizedBox(20)
            # st.text_input("Busca")

        with col3_header:
            UserPhotoWidget(
                "https://avatars.githubusercontent.com/u/63592244?v=4")
            subCol1, subCol2 = st.columns([1, 1])
            with subCol1:
                st.button("Carrinho", on_click=self.openCar)
            with subCol2:
                st.write(f"{len(st.session_state['car'])} produtos")

        col1_body, col2_body, col3_body, col4_body, col5_body = st.columns([
                                                                           1, 1, 1, 1, 1])

        with col1_body:
            st.subheader('Marcas:')
            st.write('Apple')
            st.write('Samsung')

        with col2_body:
            for product in range(0, int(len(repo.products)/4)):
                ProductWidget(
                    product=repo.products[product], car_controller=car_controller)
        with col3_body:
            for product in range(int(len(repo.products)/4), int(len(repo.products)/4 + 1*(len(repo.products)/4))):
                ProductWidget(
                    product=repo.products[product], car_controller=car_controller)
        with col4_body:
            for product in range(int(2*len(repo.products)/4), int(len(repo.products)/4 + 2*(len(repo.products)/4))):
                ProductWidget(
                    product=repo.products[product], car_controller=car_controller)
        with col5_body:
            for product in range(int(3*len(repo.products)/4), int(len(repo.products))):
                ProductWidget(
                    product=repo.products[product], car_controller=car_controller)

    def openCar(self):
        st.session_state['page'] = 'car'


def SizedBox(pixels):
    st.markdown(
        f'<div style="margin-bottom: {pixels}px"></div>',
        unsafe_allow_html=True
    )
