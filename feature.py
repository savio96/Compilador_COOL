from classe import *


class Feature(Classe):
    def __init__(self):
        super().__init__()
        self.listaExpr = []

    def adicionarExpr(self, nome):
        self.listaExpr.append(nome)
        return self.listaExpr
