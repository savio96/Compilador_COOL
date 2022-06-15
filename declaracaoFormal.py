from classe import *
class DeclaracaoFormal(Class):
    def __init__(self,id,tipo):
        super().__init__()
        self.id=id
        self.tipo=tipo


    def mostrar(self,id,tipo):
        print(id+ " : "+ tipo)