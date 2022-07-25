from classe import *
class Loop(Classe):
    def __init__(self, esq, dir,reg):
        super().__init__()
        self.esq = esq
        self.dir = dir
        self.numReg=reg
        self.flag=1

    def mostrar(self,):
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
            str1 = ".while:"
            str2  =  " "+str(self.esq)+"_"+str(self.flag)+" : bool = lt"+var1+" "+var2+":"
            str3 = " br " +self.esq+"_"+str(self.flag)+" .true.ret."+str(self.flag)+" .false.else;"
            str4 =".true.ret."+str(self.flag)+":"
            str5 = " "+var3+":"+"int = const 1"
            str6 = " "+var1+" = add "+var1+var3+";"
            str7 = " jmp .while; "
            str8 = ".false.loop:"
            str9 = " call @out_int_IO " + var1 + ";"
            vet.append(str1)
            vet.append(str2)
            vet.append(str3)
            vet.append(str4)
            vet.append(str5)
            vet.append(str6)
            vet.append(str7)
            vet.append(str8)
            vet.append(str9)
        return vet, var1
