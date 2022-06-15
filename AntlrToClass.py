from CoolParser import CoolParser
from CoolVisitor import CoolVisitor
from classe import *
from AntlrToFeature import *
from CoolParser import CoolParser
from CoolVisitor import CoolVisitor
from feature import *
from AntlrToExpr import *

class AntlrToClass(CoolVisitor):
    def __init__(self, erro,metodo,tipo):
        self.erroSemantico = erro
        self.metodo = metodo
        self.tipo=tipo
        self.variavel = {}

    def visitClasse(self, ctx: CoolParser.ClasseContext):
        classe = Class()
        featureVisitor = AntlrToFeature(self.erroSemantico,self.metodo,self.variavel,self.tipo)
        self.variavel.clear()
        for i in range(0, ctx.getChildCount()):
            if i != ctx.getChildCount() - 1:
                classe.adicionarFeature(featureVisitor.visit(ctx.getChild(i)))
        id=ctx.getChild(1).getText()
        if id not in self.tipo:
            self.tipo.append(id)
        else:
            self.erroSemantico.append("Tipo já declarado "+id)

        return classe