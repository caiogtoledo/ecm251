import streamlit as st
from src.modules.home.models.product_model import ProductModel
from src.modules.car.car_controller import CarController


def ProductWidget(product: ProductModel, car_controller: CarController):
    st.markdown(
        f"""
        <a href="#abrirModal-{product.get_name()}">
        <div 
            style="
                background: white;
                display: flex;
                justify-content: center;
                margin: 10px;
                padding: 10px; border-radius: 8px;
                flex-direction: column;
                align-items: center;
                text-decoration: none;"
            >
            <p style="text-decoration: none;">{f'{product.get_name()}'}</p>
            <img style="width: 80px; max-height: 80px" src="{product.get_photoUrl()}"/>
            <p>R$ {product.get_price()}</p>
        </div>
        </a>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
            <style>
                .modal {
                    position: fixed;
                    top: 0;
                    right: 0;
                    bottom: 0;
                    left: 0;
                    font-family: Arial, Helvetica, sans-serif;
                    background: rgba(0,0,0,0.8);
                    z-index: 99999;
                    opacity:0;
                    -webkit-transition: opacity 400ms ease-in;
                    -moz-transition: opacity 400ms ease-in;
                    transition: opacity 400ms ease-in;
                    pointer-events: none;
                    text-decoration: none;
                    }
                .modal:target {
                    opacity: 1;
                    pointer-events: auto;
                    }
                .modal > div {
                    position: relative;
                    margin: 10% auto;
                    background: #fff; 
                    width: 60vw; 
                    border-radius: 8px;
                    }
               .fechar {
                    position: absolute;
                    width: 30px;
                    right: 0px;
                    top: 0px;
                    text-align: center;
                    line-height: 30px;
                    margin: 5px;
                    background: #000;
                    border-radius: 50%;
                    font-size: 16px;
                    color: #000000;
                    text-decoration: none;
                    border: 1px;
                    border-color: #000;
                    }
            </style>
            """,
        unsafe_allow_html=True
    )
    st.markdown(
        f'''
            <div id="abrirModal-{product.get_name()}" class="modal">
                <div style="padding:10px">
                    <a href="#fechar" title="Fechar" class="fechar">x</a>
                    <h2 style="color: #000">{product.get_name()}</h2>
                    <h3 style="color: #000">{product.get_description()}</h3>
                    <h3 style="color: #000"><strong>Fabricante:</strong> {product.get_manufacturer()}<h3>
                    <h2 style="color: #000">R$ {product.get_price()}</h2>
                </div>
            </div>
            ''',
        unsafe_allow_html=True
    )
    st.button('Adicionar ao carrinho',
              key=f"{product.get_name()}",
              on_click=car_controller.add_product,
              kwargs={
                  "product": product,
              }
              )
