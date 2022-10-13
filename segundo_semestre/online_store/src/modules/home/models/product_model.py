class ProductModel():
    def __init__(self, name, price, photoUrl, description, manufacturer) -> None:
        self._name = name
        self._price = price
        self._photoUrl = photoUrl
        self._description = description
        self._manufacturer = manufacturer

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_photoUrl(self):
        return self._photoUrl

    def get_description(self):
        return self._description

    def get_manufacturer(self):
        return self._manufacturer
