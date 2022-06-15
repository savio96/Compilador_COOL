# Generated from Cool.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CoolParser import CoolParser
else:
    from CoolParser import CoolParser

# This class defines a complete generic visitor for a parse tree produced by CoolParser.

class CoolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CoolParser#Programa.
    def visitPrograma(self, ctx:CoolParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Classe.
    def visitClasse(self, ctx:CoolParser.ClasseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Metodo.
    def visitMetodo(self, ctx:CoolParser.MetodoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#DeclaracaoFeature.
    def visitDeclaracaoFeature(self, ctx:CoolParser.DeclaracaoFeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#DeclaracaoFormal.
    def visitDeclaracaoFormal(self, ctx:CoolParser.DeclaracaoFormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#MenorIgual.
    def visitMenorIgual(self, ctx:CoolParser.MenorIgualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#VariasExpr.
    def visitVariasExpr(self, ctx:CoolParser.VariasExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#NegacaoNot.
    def visitNegacaoNot(self, ctx:CoolParser.NegacaoNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Falso.
    def visitFalso(self, ctx:CoolParser.FalsoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#String.
    def visitString(self, ctx:CoolParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Subtracao.
    def visitSubtracao(self, ctx:CoolParser.SubtracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Divisao.
    def visitDivisao(self, ctx:CoolParser.DivisaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Case.
    def visitCase(self, ctx:CoolParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Verdadeiro.
    def visitVerdadeiro(self, ctx:CoolParser.VerdadeiroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Adicao.
    def visitAdicao(self, ctx:CoolParser.AdicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Igual.
    def visitIgual(self, ctx:CoolParser.IgualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#ExprChaves.
    def visitExprChaves(self, ctx:CoolParser.ExprChavesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Negacao.
    def visitNegacao(self, ctx:CoolParser.NegacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Atribuicao.
    def visitAtribuicao(self, ctx:CoolParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#ENulo.
    def visitENulo(self, ctx:CoolParser.ENuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Inteiro.
    def visitInteiro(self, ctx:CoolParser.InteiroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Loop.
    def visitLoop(self, ctx:CoolParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Multiplicacao.
    def visitMultiplicacao(self, ctx:CoolParser.MultiplicacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#NovoTipo.
    def visitNovoTipo(self, ctx:CoolParser.NovoTipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#ExprArroba.
    def visitExprArroba(self, ctx:CoolParser.ExprArrobaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Menor.
    def visitMenor(self, ctx:CoolParser.MenorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Let.
    def visitLet(self, ctx:CoolParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#Identificador.
    def visitIdentificador(self, ctx:CoolParser.IdentificadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#If.
    def visitIf(self, ctx:CoolParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#ExprParenteses.
    def visitExprParenteses(self, ctx:CoolParser.ExprParentesesContext):
        return self.visitChildren(ctx)



del CoolParser