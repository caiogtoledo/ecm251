from server.modules.products.item import Item
from server.modules.car.car import Car

# Criando objeto sem nomear os parâmetros, usando a ordem
item1 = Item('Carregador', 'Carrega Iphone e Android', 200)

# Criando objeto nomeando os parâmetros
item2 = Item(valor=300, nome='Stray', descricao='Gato')
item3 = Item(valor=300, nome='Stray', descricao='Gato')

print('Itens disponíveis')
print(item1)
print(item2)
print(item3)

car = Car()
print(f'Tamanho: {car.get_quantidade_itens()}')
print(f'Valor: {car.get_valor_total()}')

car.adicionar_item(item1)
car.adicionar_item(item2)
car.adicionar_item(item3)

print('Após adicionar no car:')
print(f'Tamanho: {car.get_quantidade_itens()}')
print(f'Valor: {car.get_valor_total()}')

car.remover(item2)

print('Após remover do car:')
print(f'Tamanho: {car.get_quantidade_itens()}')
print(f'Valor: {car.get_valor_total()}')

car.remover(item2)
