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
        listaFinal=[]
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
        for lista in self.metodo.values():
            listaFinal+=lista
        if me not in listaFinal:
            self.metodo[id] = [me]
        else:
            self.erroSemantico.append("Metodo " + me + " já existe")
        return feature

    def visitDeclaracaoFeature(self, ctx: CoolParser.DeclaracaoFeatureContext):
        feature = Feature()
        exprVisitor = AntlrToExpr(self.erroSemantico, self.metodo, self.variavel, self.tipo)
        for i in range(0, ctx.getChildCount()):
            if i != ctx.getChildCount() - 1:
                feature.adicionarExpr(exprVisitor.visit(ctx.getChild(i)))
        id = ctx.getChild(0).getText()
        tipo = ctx.getChild(2).getText()
        if tipo not in self.tipo:
            self.erroSemantico.append("Tipo nao existe " + tipo)
        if id in self.variavel:
            self.erroSemantico.append("Variavel " + id + " ja declarada!!")
        else:
            if ctx.getChildCount() < 4:
                dir2 = "none"
                valor = "none"
                self.variavel[id] = [tipo, valor]
            else:
                valor = exprVisitor.visit(ctx.getChild(4))
                dir2 = ctx.getChild(4).getText()
                tipoDir="none"
                texto=str(type(valor))
                if texto == "<class 'int'>":
                    tipoDir = 'Int'
                elif texto == "<class 'string.String_'>":
                    tipoDir = 'String'
                elif texto == "<class 'bool'>":
                    tipoDir = 'Bool'

                elif texto == "<class 'variable.Variable'>":
                    if dir2 not in self.variavel:
                        self.erroSemantico.append("Variavel " + dir2 + " nao declarada!!")
                        tipoDir = "none"
                    else:
                        for x in self.variavel.keys():
                            if x == dir2:
                                tipoDir = self.variavel[x][0]
                                valor = self.variavel[x][1]
                if tipo == tipoDir:
                    self.variavel[id] = [tipo, valor]
                else:
                    self.erroSemantico.append("Tipos incompatíveis: variável " + id + " do tipo " + tipo + " recebendo valor do tipo " + tipoDir)

        return feature
