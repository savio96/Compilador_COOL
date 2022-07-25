from classe import *
class Atribuicao(Classe):

    def __init__(self, nome, expr,atributoClasse,this):
        super().__init__()
        self.nome=nome
        self.expr=expr
        self.atributoClasse=atributoClasse
        self.thisReg=this

    def mostrar(self):
        linha=""
        for x in self.atributoClasse.values():
            lista = x[0]
            if self.nome in lista:
                pos=lista.index(self.nome)
                if pos==0:
                    linha="store this "+self.expr+";"
                else:
                    this="this"+str(self.thisReg[0])
                    linha="inc: int = const "+str(pos)+";\n"
                    linha+=this+" : ptr<int> = ptradd this inc;\n"
                    linha+="store "+this+" "+self.expr+";"
                    self.thisReg[0]=self.thisReg[0]+1
        return linha


