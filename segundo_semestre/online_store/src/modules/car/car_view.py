# Nome: Caio B B G de Toledo
# RA: 20.01430-9

import streamlit as st
from src.modules.car.car_controller import CarController


class CarView():
    def __init__(self, car_controller: CarController) -> None:
        st.button('←', on_click=self.closeCar)
        st.title('Carrinho')
        if len(st.session_state['car']) == 0:
            st.subheader('Você não possui produtos no carrinho')
        else:
            col1, col2, col3 = st.columns(3)
            i = 0
            for product in st.session_state['car']:
                with st.container():
                    col1.write(f'{product.get_name()}')
                    col1.markdown(
                        f'<div style="margin-bottom: 1.63rem"></div>',
                        unsafe_allow_html=True
                    )
                    col2.write(f'{product.get_price()}')
                    col2.markdown(
                        f'<div style="margin-bottom: 1.63rem"></div>',
                        unsafe_allow_html=True
                    )
                    col3.button('✘',
                                key=f'{product.get_name()+str(i)+str(i)}',
                                on_click=car_controller.remove_product,
                                kwargs={'product_to_remove': product}
                                )
                    col3.markdown(
                        f'<div style="margin-bottom: 1rem"></div>',
                        unsafe_allow_html=True
                    )
                i += 1
            st.subheader(f'Total: R$ {car_controller.get_total_price()}')
            st.button('Finalizar compra',
                      on_click=car_controller.finalize_purchase)

    def closeCar(self):
        st.session_state['page'] = 'home'


def SizedBox(pixels):
    st.markdown(
        f'<div style="margin-bottom: {pixels}px"></div>',
        unsafe_allow_html=True
    )
