from classe import *
class Igual(Classe):
    def __init__(self, esq,dir,reg):
        super().__init__()
        self.esq = esq
        self.dir = dir
        self.numReg=reg


    def mostrar(self):
        var1 = 'v' + str(self.numReg[0])
        self.numReg[0] = self.numReg[0] + 1
        var2 = 'v' + str(self.numReg[0])
        self.numReg[0] = self.numReg[0] + 1
        var3 = 'v' + str(self.numReg[0])
        self.numReg[0] = self.numReg[0] + 1
        vet = []
        registradores = ["v0", "v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10"]
        if self.esq in registradores and self.dir in registradores:
            var1 = self.esq
            var2 = self.dir
        else:
            str1 = var1 + ': int = const ' + self.esq + ';'
            str2 = var2 + ': int = const ' + self.dir + ';'
            vet.append(str1)
            vet.append(str2)
        str3= var3+" : bool  = eq "+ var1+" "+var2+";"
        vet.append(str3)
        return vet,var3