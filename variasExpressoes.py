from classe import *
class VariasExpressoes(Class):
    def __init__(self,vetor):
        super().__init__()
        self.vetor=vetor


    def mostrar(self,vetor):
        print("Expr: "+ vetor)