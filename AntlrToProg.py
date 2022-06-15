from AntlrToClass import *
from AntlrToProg import *
from program import *


class AntlrToProg(CoolVisitor):
    def __init__(self):
        self.erroSemantico = []
        self.tipo=["Int","String","Object","IO","Bool"]
        self.metodos = {}
        self.metodos["String"]=["length","concat","substr"]
        self.metodos["Object"]=["type_name","copy"]
        self.metodos["IO"]=["out_string","out_int","in_string","in_int"]


    def visitPrograma(self, ctx: CoolParser.ProgramaContext):
        prog = Program()
        classVisitor = AntlrToClass(self.erroSemantico, self.metodos,self.tipo)
        for i in range(0, ctx.getChildCount()):
            if i != ctx.getChildCount() - 1:
                prog.adicionarClasses(classVisitor.visit(ctx.getChild(i)))
        return prog

    def mostrar(self):
        if len(self.erroSemantico)!=0:
            print("Error:")
            for i in self.erroSemantico:
                print(i)
        else:
            print("Fim do processo de Analise Semantica")
