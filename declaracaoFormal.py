from classe import *
class DeclaracaoFormal(Classe):
    def __init__(self,id,tipo):
        super().__init__()
        self.id=id
        self.tipo=tipo


    def mostrar(self):
        if self.tipo=="Int":
            linha=', '+self.id+': int'
        else:
            linha=', '+self.id+': ptr<int>'
        return linha
        #print(id+ " : "+ tipo)