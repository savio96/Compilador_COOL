from classe import *
class IfCon(Classe):
    def __init__(self, esq,meio,dir,reg):
        super().__init__()
        self.esq = esq
        self.meio=meio
        self.dir = dir
        self.numReg=reg
        self.flag=1

    def mostrar(self):
        var1 = 'v' + str(self.numReg[0])
        self.numReg[0] = self.numReg[0] + 1
        var2 = 'v' + str(self.numReg[0])
        self.numReg[0] = self.numReg[0] + 1
        vet = []
        registradores = ["v0", "v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10"]
        if self.esq in registradores and self.dir in registradores:
            var1 = self.esq
            var2 = self.dir
        else:
            str1 = "br " +self.esq+"_"+str(self.flag)+" .true.ret."+str(self.flag)+" .false.else;"
            str2 = ".true.ret."+str(self.flag)+":"
            str3 = "call @out_int_IO "+ var1+";"
            str4=".false.else:"
            str5="call @out_int_IO "+ var2+";"
            vet.append(str1)
            vet.append(str2)
            vet.append(str3)
            vet.append(str4)
            vet.append(str5)
        return vet,var1,var2