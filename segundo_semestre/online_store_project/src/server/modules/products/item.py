import random


class Item():
    def __init__(self, nome, descricao, valor) -> None:
        self._id = random.randint(0, 9999)
        self._valor = valor
        self._descricao = descricao
        self._nome = nome

    def get_valor(self):
        return self._valor

    def get_descricao(self):
        return self._descricao

    def get_nome(self):
        return self._nome

    def get_id(self):
        return self._id

    def __str__(self) -> str:
        return f'{self._nome}, {self._valor} reais e id: {self._id}'
