from program import *


class Classe(Program):
    def __init__(self):
        super().__init__()
        self.listaFeature = []

    def adicionarFeature(self, nome):
        self.listaFeature.append(nome)
        return self.listaFeature
