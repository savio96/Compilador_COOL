from string import String_
from CoolParser import CoolParser
from CoolVisitor import CoolVisitor
from antlr4 import *
from loop import *
from variable import *
from soma import *
from atribuicao import *
from subtracao import *
from divisao import *
from menor import *
from multiplication import *
from menorIgual import *
from igual import *
from string import *
from exprParenteses import *
from negacaoNot import *
from negacao import *
from enulo import *
from ifCon import *
from ExprChaves import *
from declaracaoFormal import *
from variasExpressoes import *


class AntlrToExpr(CoolVisitor):

    def __init__(self, erro, metodo, variavel, tipo):
        super().__init__()
        self.variavel = variavel
        self.tipos = []
        self.metodo = metodo
        self.erros_semanticos = erro
        self.tipo = tipo

    def visitDeclaracaoFormal(self, ctx: CoolParser.DeclaracaoFormalContext):
        id = ctx.getChild().getText()
        tipo = ctx.getChild(2).getText()
        if tipo not in self.tipo:
            self.erros_semanticos.append("Tipo nao existe " + tipo)
        if id in self.variavel:
            self.erros_semanticos.append("Variavel " + id + " ja declarada!!")
        else:
            self.variavel[id] = [tipo, "none"]
        return DeclaracaoFormal(id, tipo)

    def visitMenorIgual(self, ctx: CoolParser.MenorIgualContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        esq = exprVisitor.visit(ctx.getChild(0))
        dir = exprVisitor.visit(ctx.getChild(2))
        return MenorIgual(esq, dir)

    def visitVariasExpr(self, ctx: CoolParser.VariasExprContext):
        variasExpr = []
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        id = ctx.getChild(0).getText()
        variasExpr.append(id)
        for i in range(2, ctx.getChildCount() - 1):
            if ctx.getChild(i).getText() != ",":
                var = exprVisitor.visit(ctx.getChild(i))
                variasExpr.append(var)
        return ExprChaves(variasExpr)

    def visitNegacaoNot(self, ctx: CoolParser.NegacaoNotContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        var = exprVisitor.visit(ctx.getChild(1))
        return NegacaoNot(var)

    def visitFalso(self, ctx: CoolParser.FalsoContext):
        return False

    def visitString(self, ctx: CoolParser.StringContext):
        str = ctx.getChild(0).getText()
        return String_(str)

    def visitSubtracao(self, ctx: CoolParser.SubtracaoContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        esq = exprVisitor.visit(ctx.getChild(0))
        dir = exprVisitor.visit(ctx.getChild(2))
        return Subtracao(esq, dir)

    def visitDivisao(self, ctx: CoolParser.DivisaoContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        esq = exprVisitor.visit(ctx.getChild(0))
        dir = exprVisitor.visit(ctx.getChild(2))
        return Divisao(esq, dir)

    def visitCase(self, ctx: CoolParser.CaseContext):
        return super().visitCase(ctx)

    def visitVerdadeiro(self, ctx: CoolParser.VerdadeiroContext):
        return True

    def visitAdicao(self, ctx: CoolParser.AdicaoContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        esq = exprVisitor.visit(ctx.getChild(0))
        dir = exprVisitor.visit(ctx.getChild(2))
        return Soma(esq, dir)

    def visitIgual(self, ctx: CoolParser.IgualContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        esq = exprVisitor.visit(ctx.getChild(0))
        dir = exprVisitor.visit(ctx.getChild(2))
        return Igual(esq, dir)

    def visitExprChaves(self, ctx: CoolParser.ExprChavesContext):
        expr = []
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)

        for i in range(1, ctx.getChildCount() - 1):
            if ctx.getChild(i).getText() != ";":
                var = exprVisitor.visit(ctx.getChild(i))
                expr.append(var)
        return ExprChaves(expr)

    def visitNegacao(self, ctx: CoolParser.NegacaoContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        var = exprVisitor.visit(ctx.getChild(1))
        return Negacao(var)

    def visitAtribuicao(self, ctx: CoolParser.AtribuicaoContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        esq = ctx.getChild(0).getText()
        dir = exprVisitor.visit(ctx.getChild(2))
        dir2=ctx.getChild(2).getText()
        valor=dir
        if esq not in self.variavel:
            self.erros_semanticos.append("Variavel " + esq + " nao declarada!!")
        else:
            for id in self.variavel.keys():
                if id==esq:
                    tipoVar = self.variavel[id][0]
                    texto=str(type(dir))
                    if texto == "<class 'int'>":
                        tipoDir = 'Int'
                    elif texto == "<class 'string.String_'>":
                        tipoDir = 'String'
                    elif texto =="<class 'bool'>":
                        tipoDir = 'Bool'

                    elif texto =="<class 'variable.Variable'>":
                        if dir2 not in self.variavel:
                            self.erros_semanticos.append("Variavel " + dir2 + " nao declarada!!")
                            tipoDir="none"
                        else:
                            for x in self.variavel.keys():
                                if x==dir2:
                                    tipoDir = self.variavel[x][0]
                                    valor=self.variavel[x][1]

                    if tipoVar==tipoDir:
                        self.variavel[id][1]=valor
                        print(self.variavel)
                    else:
                        self.erros_semanticos.append("Tipos incompatíveis: variável " + id + " do tipo " +tipoVar+ " recebendo valor do tipo " + tipoDir)
        return Atribuicao(esq, dir)

    def visitENulo(self, ctx: CoolParser.ENuloContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        var = exprVisitor.visit(ctx.getChild(1))
        return Enulo(var)

    def visitInteiro(self, ctx: CoolParser.InteiroContext):
        numText = ctx.getChild(0).getText()
        num = int(numText)
        return num

    def visitLoop(self, ctx: CoolParser.LoopContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        esq = exprVisitor.visit(ctx.getChild(1))
        dir = exprVisitor.visit(ctx.getChild(3))
        return Loop(esq, dir)

    def visitMultiplicacao(self, ctx: CoolParser.MultiplicacaoContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        esq = exprVisitor.visit(ctx.getChild(0))
        dir = exprVisitor.visit(ctx.getChild(2))
        return Multiplication(esq, dir)

    def visitNovoTipo(self, ctx: CoolParser.NovoTipoContext):
        var = ctx.getChild(1).getText()
        if var not in self.tipo:
            self.tipo.append(var)
        else:
            self.erros_semanticos.append("Tipo já declarado " + var)
        return super().visitNovoTipo(ctx)

    def visitExprArroba(self, ctx: CoolParser.ExprArrobaContext):
        return super().visitExprArroba(ctx)

    def visitMenor(self, ctx: CoolParser.MenorContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        esq = exprVisitor.visit(ctx.getChild(0))
        dir = exprVisitor.visit(ctx.getChild(2))
        return Menor(esq, dir)

    def visitLet(self, ctx: CoolParser.LetContext):
        return super().visitLet(ctx)

    def visitIdentificador(self, ctx: CoolParser.IdentificadorContext):
        id = ctx.getChild(0).getText()
        if id not in self.variavel:
            self.erros_semanticos.append("variavel " + id + " nao declarada!!")
        return Variable(id)

    def visitIf(self, ctx: CoolParser.IfContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        esq = exprVisitor.visit(ctx.getChild(1))
        meio = exprVisitor.visit(ctx.getChild(3))
        dir = exprVisitor.visit(ctx.getChild(5))

        return IfCon(esq, meio, dir)

    def visitExprParenteses(self, ctx: CoolParser.ExprParentesesContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo)
        var = exprVisitor.visit(ctx.getChild(1))
        return ExprParenteses(var)
