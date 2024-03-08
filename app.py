from modelos.restaurantes import Restaurante
from modelos.Cardapio.Prato import Prato
from modelos.Cardapio.Bebida import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')
pratos = Prato('Cuscuz',45,'Muito Gostoso')
bebidas = Bebida('Agua',8,'Gelada ou Natural')
restaurante_praca.adicionar_no_cardapio(bebidas)
restaurante_praca.adicionar_no_cardapio(pratos)


def main():
    print(pratos,bebidas)

if __name__ == '__main__':
    main()