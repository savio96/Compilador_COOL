from classe import *
class ExprArroba(Classe):
    def __init__(self,id,metodosCool):
        super().__init__()
        self.id = id
        self.metodosCool=metodosCool

    def pegarChave(self,val):
        for chave,valor in self.metodosCool.items():
            if val==valor:
                return chave
        return ""
    def mostrar(self):
        p=self.pegarChave(self.id)
        linha="@"+self.id+"_"+p

        return linha
