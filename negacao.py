from classe import *
class Negacao(Classe):
    def __init__(self, string):
        super().__init__()
        self.string=string

    def mostrar(self,string):
        print('~'+ string)