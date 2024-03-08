from abc import ABC,abstractmethod

class Itemcardapio(ABC):
    def __init__(self,nome,preco):
       self.Nome = nome
       self.Preco = preco

    @abstractmethod
    def desconto_cardapio(self):
        pass


      