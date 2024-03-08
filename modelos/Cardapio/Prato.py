from modelos.Cardapio.item_cardapio import Itemcardapio

class Prato(Itemcardapio): 
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self.descricao = descricao
    
    def __str__(self): 
        return self.Nome
    
    def desconto_cardapio(self):
        self.Preco -= self.Preco *0.08