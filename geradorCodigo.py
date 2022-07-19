from AntlrToProg import *

class GeradorCodigo():
    def __init__(self,geraCodigo):
        super().__init__()
        self.geraCodigo=geraCodigo

    def geraCod(self):
        arq=open("saida.txt","w")

        #print(self.geraCodigo)
        for i in self.geraCodigo:
            arq.write(i)
            arq.write("\n")




