from classe import *



class Program():
    def __init__(self):
        super().__init__()
        self.listaClass = []

    def adicionarClasses(self, nome):
        self.listaClass.append(nome)
        return self.listaClass
