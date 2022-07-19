from classe import *
class Variable(Classe):
    def __init__(self, id,atributoClasse,reg,this,variavel):
        super().__init__()
        self.id=id
        self.atributoClasse=atributoClasse
        self.numReg=reg
        self.thisReg = this
        self.variavel=variavel


    def mostrar(self):
        linha=""
        reg=self.id
        #print(self.id)

        
        registradores=["v0","v1","v2","v3","v4","v5","v6","v7","v8","v9","v10"]
        if self.id in self.variavel.keys():
            valor=self.variavel.get(self.id)[1]
            if valor!="none" and valor in registradores:
                linha+=""
                reg=valor
            else:
                for x in self.atributoClasse.values():
                    lista = x[0]
                    if self.id in lista:
                        pos=lista.index(self.id)
                        this = "this" + str(self.thisReg[0])
                        self.thisReg[0]=self.thisReg[0]+1
                        linha="inc: int = const "+str(pos)+";\n"
                        linha+=this+": ptr<int> = ptradd this inc;\n"
                        reg="v"+str(self.numReg[0])
                        linha+=reg+": int = load "+this+";"
                        self.numReg[0]=self.numReg[0]+1
                    #print(self.variavel)
        return linha,reg