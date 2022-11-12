import sqlite3
from src.modules.home.models.product_model import ProductModel


class ProductDAO:

    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = ProductDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db')

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM product;
        """)
        responses = []
        for res in self.cursor.fetchall():
            responses.append(
                ProductModel(
                    id=res[0],
                    name=res[1],
                    price=res[2],
                    category=res[3],
                    description=res[4],
                    manufacturer=res[5],
                    photoUrl=res[6]
                )
            )
        self.cursor.close()
        return responses

    def add_product(self, product: ProductModel):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO product (
                SKU,
                name,
                price,
                category,
                description,
                manufacturer,
                urlPic
            )
            VALUES(?,?,?,?,?,?,?);
        """, (
            product.get_id(),
            product.get_name(),
            product.get_price(),
            product.get_category(),
            product.get_description(),
            product.get_manufacturer(),
            product.get_photoUrl()
        ))
        self.conn.commit()
        self.cursor.close()

    # def pegar_item(self, id):
    #     self.cursor = self.conn.cursor()
    #     self.cursor.execute(f"""
    #         SELECT * FROM Itens
    #         WHERE id = '{id}';
    #     """)
    #     item = None
    #     resultado = self.cursor.fetchone()
    #     if resultado:
    #         item = Item(id=resultado[0], nome=resultado[1], preco=resultado[2])
    #     self.cursor.close()
    #     return item

    def atualizar_item(self, product: ProductModel):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE product SET 
                name = '{product.get_name()}',
                price = {product.get_price()},
                category = {product.get_category()},
                description = {product.get_description()},
                manufacturer = {product.get_manufacturer()},
                urlPic = {product.get_photoUrl()}
                WHERE id = '{product.get_id()}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def deletar_item(self, id):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM product
                Where id = '{id}'  
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    # def search_all_for_name(self, nome):
    #     self.cursor = self.conn.cursor()
    #     self.cursor.execute(f"""
    #         SELECT * FROM product
    #         WHERE nome LIKE '{nome}%';
    #     """)
    #     resultados = []
    #     for resultado in self.cursor.fetchall():
    #         resultados.append(
    #             Item(id=resultado[0], nome=resultado[1], preco=resultado[2]))
    #     self.cursor.close()
    #     return resultados
