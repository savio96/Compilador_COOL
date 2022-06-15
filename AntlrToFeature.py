from CoolParser import CoolParser
from CoolVisitor import CoolVisitor
from feature import *
from AntlrToExpr import *


class AntlrToFeature(CoolVisitor):
    def __init__(self, erro, metodo, variavel, tipo):
        self.erroSemantico = erro
        self.metodo = metodo
        self.variavel = variavel
        self.tipo = tipo

    def visitMetodo(self, ctx: CoolParser.MetodoContext):
        feature = Feature()
        exprVisitor = AntlrToExpr(self.erroSemantico, self.metodo, self.variavel, self.tipo)
        for i in range(0, ctx.getChildCount()):
            if i != ctx.getChildCount() - 1:
                feature.adicionarExpr(exprVisitor.visit(ctx.getChild(i)))
        var = ctx.TYPE().getText()
        if var not in self.tipo:
            self.erroSemantico.append("Tipo nao existe " + var)
        me = ctx.ID().getText()
        id = ctx.getText()
        if me not in self.metodo:
            self.metodo[id] = [me]
        else:
            self.erroSemantico.append("Metodo " + me + " já existe na classe " + id)
        return feature

    def visitDeclaracaoFeature(self, ctx: CoolParser.DeclaracaoFeatureContext):
        feature = Feature()
        exprVisitor = AntlrToExpr(self.erroSemantico, self.metodo, self.variavel, self.tipo)
        for i in range(0, ctx.getChildCount()):
            if i != ctx.getChildCount() - 1:
                feature.adicionarExpr(exprVisitor.visit(ctx.getChild(i)))
        id = ctx.getChild(0).getText()
        tipo = ctx.getChild(2).getText()
        if ctx.getChildCount() > 4:
            valor = exprVisitor.visit(ctx.getChild(4))
        else:
            valor = "none"
        if tipo not in self.tipo:
            self.erroSemantico.append("Tipo nao existe " + tipo)
        if id in self.variavel:
            self.erroSemantico.append("Variavel " + id + " ja declarada!!")
        else:
            self.variavel[id] = [tipo, valor]
        return feature
