from classe import *
class Case(Classe):

    def __init__(self, expr, id, tipo,expr2):
        super().__init__()
        self.expr=expr
        self.id = id
        self.tipo=tipo
        self.expr2 = expr2

    def mostrar(self,expr, id, tipo,expr2):
        pass