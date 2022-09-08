from item import Item
from carrinho import Carrinho

# Criando objeto sem nomear os parâmetros, usando a ordem
item1 = Item('Carregador', 'Carrega Iphone e Android', 200)

# Criando objeto nomeando os parâmetros
item2 = Item(valor=300, nome='Stray', descricao='Gato')
item3 = Item(valor=300, nome='Stray', descricao='Gato')

print('Itens disponíveis')
print(item1)
print(item2)
print(item3)

carrinho = Carrinho()
print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')

carrinho.adicionar_item(item1)
carrinho.adicionar_item(item2)
carrinho.adicionar_item(item3)

print('Após adicionar no carrinho:')
print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')

carrinho.remover(item2)

print('Após remover do carrinho:')
print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')

carrinho.remover(item2)
