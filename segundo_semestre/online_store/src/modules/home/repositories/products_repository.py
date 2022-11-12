# Nome: Caio B B G de Toledo
# RA: 20.01430-9

from src.modules.home.models.product_model import ProductModel
from typing import List
from src.dao.product_dao import ProductDAO


class ProductsRepository():
    products: List[ProductModel]

    def __init__(self) -> None:
        self.products = ProductDAO().get_all()
