from classe import *
class Negacao(Class):
    def __init__(self, string):
        super().__init__()
        self.string=string

    def mostrar(self,string):
        print('~'+ string)