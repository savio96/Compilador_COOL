from classe import *
class VariableFeatureDecla(Class):

    def __init__(self, nome, tipo, valor):
        super().__init__()
        self.nome=nome
        self.tipo=tipo
        self.expr = valor

    def mostrar(self,nome,tipo,expr):
        print(nome+" : "+tipo+" <- "+expr)