# Nome: Caio B B G de Toledo
# RA: 20.01430-9

class ProductModel():
    def __init__(self, id, name, price, category, photoUrl, description, manufacturer) -> None:
        self._id = id
        self._name = name
        self._price = str(price)
        self._category = category
        self._photoUrl = photoUrl
        self._description = description
        self._manufacturer = manufacturer

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_price(self):
        return str(self._price)

    def get_category(self):
        return self._category

    def get_photoUrl(self):
        return self._photoUrl

    def get_description(self):
        return self._description

    def get_manufacturer(self):
        return self._manufacturer
