from classe import *
class Subtracao(Class):
    def __init__(self, esq,dir):
        super().__init__()
        self.esq = esq
        self.dir = dir

    def mostrar(self,esq,dir):
        print(esq+" - "+dir)