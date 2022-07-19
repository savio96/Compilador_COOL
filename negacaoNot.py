from classe import *
class NegacaoNot(Classe):
    def __init__(self, string):
        super().__init__()
        self.string=string

    def mostrar(self,string):
        print('not '+ string)