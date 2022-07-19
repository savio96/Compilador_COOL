from AntlrToClass import *
from CoolParser import *
from program import *
from geradorCodigo import *


class AntlrToProg(CoolVisitor, Program):
    def __init__(self):
        super().__init__()
        self.erroSemantico = []
        self.geraCodigo = []
        self.tipo = ["Int", "String", "Object", "IO", "Bool"]
        self.metodos = {}
        self.metodos["String"] = ["length", "concat", "substr"]
        self.metodos["Object"] = ["type_name", "copy"]
        self.metodos["IO"] = ["out_string", "out_int", "in_string", "in_int"]
        self.metodosCool = {}
        self.metodosCool["String"] = ["length", "concat", "substr"]
        self.metodosCool["Object"] = ["type_name", "copy"]
        self.metodosCool["IO"] = ["out_string", "out_int", "in_string", "in_int"]
        self.outMain = ""
        self.qtdParam = {}
        self.atributoClasse={}
        self.herancaOO={}

    def visitPrograma(self, ctx: CoolParser.ProgramaContext):
        prog = Program()
        classVisitor = AntlrToClass(self.erroSemantico, self.metodos, self.tipo, self.geraCodigo, self.metodosCool,
                                    self.geraCodigo,self.qtdParam,self.atributoClasse,self.herancaOO)
        for i in range(0, ctx.getChildCount()):
            if i != ctx.getChildCount() - 1:
                prog.adicionarClasses(classVisitor.visit(ctx.getChild(i)))

        return prog

    def mostrar(self):
        """
        if len(self.erroSemantico) != 0:
            print("Error:")
            for i in self.erroSemantico:
                print(i)

        else:
        """
        #print("Fim do processo de Analise Semantica")
        cod = GeradorCodigo(self.geraCodigo)
        cod.geraCod()
        print("Fim do processo de Geracao de codigo")
