from classe import *

class Number(Classe):
    def __init__(self, num,reg):
        super().__init__()
        self.num=str(num)
        self.numReg=reg

    def mostrar(self):
        var1 = 'v' + str(self.numReg[0])
        self.numReg[0]=self.numReg[0]+1
        linha=var1 +" : int = const "+self.num+";"
        return linha,var1