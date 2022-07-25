from classe import *
class Let(Classe):
    def __init__(self, id,tipo,valor,variavel):
        super().__init__()
        self.id = id
        self.tipo=tipo
        self.valor = valor
        self.variavel=variavel

    def mostrar(self):
        print(self.variavel)