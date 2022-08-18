
class Carrinho():
    # Método construtor
    def __init__(self) -> None:
        self._itens = []
    # Métodos da classe

    def get_valor_total(self):
        valores = [item.get_valor() for item in self._itens]
        return sum(valores)

    def get_quantidade_itens(self):
        return len(self._itens)

    def adicionar_item(self, item):
        self._itens.append(item)

    def remover(self, item):
        if item in self._itens:
            self._itens.remove(item)
        else:
            print('Não existe o item no carrinho')
