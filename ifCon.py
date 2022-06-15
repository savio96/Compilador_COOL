from classe import *
class IfCon(Class):
    def __init__(self, esq,meio,dir):
        super().__init__()
        self.esq = esq
        self.meio=meio
        self.dir = dir

    def mostrar(self,esq,meio,dir):
        print("if "+esq+" then"+meio+" else "+dir+" fi ")