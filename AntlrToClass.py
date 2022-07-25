from CoolParser import CoolParser
from CoolVisitor import CoolVisitor
from classe import *
from AntlrToFeature import *
from CoolParser import CoolParser
from CoolVisitor import CoolVisitor
from feature import *
from AntlrToExpr import *
from collections import deque


class AntlrToClass(CoolVisitor):
    def __init__(self, erro, metodo, tipo, geraCodigo, metodosCool, outMain, qtdParam,atributoClasse,herancaOO):
        super().__init__()
        self.erroSemantico = erro
        self.metodo = metodo
        self.tipo = tipo
        self.geraCodigoClasse = []
        self.geraCodigoProg = geraCodigo
        self.variavel = {}
        self.metodosCool = metodosCool
        self.outMain = outMain
        self.qtdParam = qtdParam
        self.atributoClasse=atributoClasse
        self.numReg = [0]
        self.thisReg = [1]
        self.herancaOO=herancaOO

    def visitClasse(self, ctx: CoolParser.ClasseContext):
        classe = Classe()
        id = ctx.getChild(1).getText()

        #Condição para adicionar as classes herdadas
        if "inherits" in ctx.getText():
            self.herancaOO[id]=ctx.getChild(3).getText()

        if id not in self.tipo:
            self.tipo.append(id)
        else:
            self.erroSemantico.append("Tipo já declarado " + id)
        featureVisitor = AntlrToFeature(self.erroSemantico, self.metodo, self.variavel, self.tipo, id,
                                        self.geraCodigoClasse, self.metodosCool, self.outMain, self.qtdParam,self.atributoClasse,
                                        self.numReg,self.thisReg,self.herancaOO)
        self.variavel.clear()

        for i in range(0, ctx.getChildCount()):
            if i != ctx.getChildCount() - 1:
                classe.adicionarFeature(featureVisitor.visit(ctx.getChild(i)))

        # geração de código
        self.geraCodigoProg.extend(self.geraCodigoClasse)
        self.geraCodigoClasse = []
        return classe

