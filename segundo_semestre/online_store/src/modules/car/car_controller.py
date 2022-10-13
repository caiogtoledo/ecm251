import streamlit as st
from src.modules.home.models.product_model import ProductModel


class CarController():
    def __init__(self) -> None:
        if 'car' not in st.session_state:
            st.session_state['car'] = []

    def add_product(self, product: ProductModel):
        # if 'car' not in st.session_state:
        #     st.session_state['car'] = []
        products = st.session_state['car']
        print('products before add:', products)
        products.append(product)
        print('products after add: ', products)
        st.session_state['car'] = products

    def remove_product(self, product_to_remove):
        if product_to_remove in st.session_state['car']:
            products = st.session_state['car']
            products.remove(product_to_remove)
        st.session_state['car'] = products

    def get_total_price(self):
        total = 0
        for product in st.session_state['car']:
            total += round(float(product.get_price().replace('.', '')), 2)
        return str(total).replace('.', ',')

    def finalize_purchase(self):
        # Por enquanto apenas apagando o carrinho
        # To Do: abrir tela de pagamento
        st.session_state['car'] = []
        st.session_state['page'] = 'success'
