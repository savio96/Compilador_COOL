from classe import *
class VariasExpressoes(Classe):
    def __init__(self,id,metodosCool):
        super().__init__()
        self.id = id
        self.metodosCool=metodosCool
        self.nomeFuncao=""

    def pegarChave(self,val):
        for chave,valor in self.metodosCool.items():
            if val in valor:
                return chave
        return ""

    def insereMetodo(self):
        p=self.pegarChave(self.id)
        linha="@"+self.id+"_"+p+"(this: int) { print this; }"
        self.nomeFuncao=self.id+"_"+p
        return linha

    def montarMetodosHeranca(self):
        #self.listaFeature
            pass
    def mostrar(self,var):
        p = self.pegarChave(self.id)
        self.nomeFuncao = self.id + "_" + p
        linha="call @"+self.nomeFuncao+" "+var+";"
        #print(linha)

        return linha