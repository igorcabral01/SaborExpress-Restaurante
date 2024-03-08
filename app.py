from modelos.restaurantes import Restaurante
from modelos.Cardapio.Prato import Prato
from modelos.Cardapio.Bebida import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')
pratos = Prato('Cuscuz',45,'Muito Gostoso')
pratos.desconto_cardapio()
bebidas = Bebida('Agua',8,'Gelada ou Natural')
bebidas.desconto_cardapio()
restaurante_praca.adicionar_no_cardapio(bebidas)
restaurante_praca.adicionar_no_cardapio(pratos)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()