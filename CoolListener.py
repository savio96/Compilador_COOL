# Generated from Cool.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CoolParser import CoolParser
else:
    from CoolParser import CoolParser

# This class defines a complete listener for a parse tree produced by CoolParser.
class CoolListener(ParseTreeListener):

    # Enter a parse tree produced by CoolParser#Programa.
    def enterPrograma(self, ctx:CoolParser.ProgramaContext):
        pass

    # Exit a parse tree produced by CoolParser#Programa.
    def exitPrograma(self, ctx:CoolParser.ProgramaContext):
        pass


    # Enter a parse tree produced by CoolParser#Classe.
    def enterClasse(self, ctx:CoolParser.ClasseContext):
        pass

    # Exit a parse tree produced by CoolParser#Classe.
    def exitClasse(self, ctx:CoolParser.ClasseContext):
        pass


    # Enter a parse tree produced by CoolParser#Metodo.
    def enterMetodo(self, ctx:CoolParser.MetodoContext):
        pass

    # Exit a parse tree produced by CoolParser#Metodo.
    def exitMetodo(self, ctx:CoolParser.MetodoContext):
        pass


    # Enter a parse tree produced by CoolParser#DeclaracaoFeature.
    def enterDeclaracaoFeature(self, ctx:CoolParser.DeclaracaoFeatureContext):
        pass

    # Exit a parse tree produced by CoolParser#DeclaracaoFeature.
    def exitDeclaracaoFeature(self, ctx:CoolParser.DeclaracaoFeatureContext):
        pass


    # Enter a parse tree produced by CoolParser#DeclaracaoFormal.
    def enterDeclaracaoFormal(self, ctx:CoolParser.DeclaracaoFormalContext):
        pass

    # Exit a parse tree produced by CoolParser#DeclaracaoFormal.
    def exitDeclaracaoFormal(self, ctx:CoolParser.DeclaracaoFormalContext):
        pass


    # Enter a parse tree produced by CoolParser#MenorIgual.
    def enterMenorIgual(self, ctx:CoolParser.MenorIgualContext):
        pass

    # Exit a parse tree produced by CoolParser#MenorIgual.
    def exitMenorIgual(self, ctx:CoolParser.MenorIgualContext):
        pass


    # Enter a parse tree produced by CoolParser#VariasExpr.
    def enterVariasExpr(self, ctx:CoolParser.VariasExprContext):
        pass

    # Exit a parse tree produced by CoolParser#VariasExpr.
    def exitVariasExpr(self, ctx:CoolParser.VariasExprContext):
        pass


    # Enter a parse tree produced by CoolParser#NegacaoNot.
    def enterNegacaoNot(self, ctx:CoolParser.NegacaoNotContext):
        pass

    # Exit a parse tree produced by CoolParser#NegacaoNot.
    def exitNegacaoNot(self, ctx:CoolParser.NegacaoNotContext):
        pass


    # Enter a parse tree produced by CoolParser#Falso.
    def enterFalso(self, ctx:CoolParser.FalsoContext):
        pass

    # Exit a parse tree produced by CoolParser#Falso.
    def exitFalso(self, ctx:CoolParser.FalsoContext):
        pass


    # Enter a parse tree produced by CoolParser#String.
    def enterString(self, ctx:CoolParser.StringContext):
        pass

    # Exit a parse tree produced by CoolParser#String.
    def exitString(self, ctx:CoolParser.StringContext):
        pass


    # Enter a parse tree produced by CoolParser#Subtracao.
    def enterSubtracao(self, ctx:CoolParser.SubtracaoContext):
        pass

    # Exit a parse tree produced by CoolParser#Subtracao.
    def exitSubtracao(self, ctx:CoolParser.SubtracaoContext):
        pass


    # Enter a parse tree produced by CoolParser#Divisao.
    def enterDivisao(self, ctx:CoolParser.DivisaoContext):
        pass

    # Exit a parse tree produced by CoolParser#Divisao.
    def exitDivisao(self, ctx:CoolParser.DivisaoContext):
        pass


    # Enter a parse tree produced by CoolParser#Case.
    def enterCase(self, ctx:CoolParser.CaseContext):
        pass

    # Exit a parse tree produced by CoolParser#Case.
    def exitCase(self, ctx:CoolParser.CaseContext):
        pass


    # Enter a parse tree produced by CoolParser#Verdadeiro.
    def enterVerdadeiro(self, ctx:CoolParser.VerdadeiroContext):
        pass

    # Exit a parse tree produced by CoolParser#Verdadeiro.
    def exitVerdadeiro(self, ctx:CoolParser.VerdadeiroContext):
        pass


    # Enter a parse tree produced by CoolParser#Adicao.
    def enterAdicao(self, ctx:CoolParser.AdicaoContext):
        pass

    # Exit a parse tree produced by CoolParser#Adicao.
    def exitAdicao(self, ctx:CoolParser.AdicaoContext):
        pass


    # Enter a parse tree produced by CoolParser#Igual.
    def enterIgual(self, ctx:CoolParser.IgualContext):
        pass

    # Exit a parse tree produced by CoolParser#Igual.
    def exitIgual(self, ctx:CoolParser.IgualContext):
        pass


    # Enter a parse tree produced by CoolParser#ExprChaves.
    def enterExprChaves(self, ctx:CoolParser.ExprChavesContext):
        pass

    # Exit a parse tree produced by CoolParser#ExprChaves.
    def exitExprChaves(self, ctx:CoolParser.ExprChavesContext):
        pass


    # Enter a parse tree produced by CoolParser#Negacao.
    def enterNegacao(self, ctx:CoolParser.NegacaoContext):
        pass

    # Exit a parse tree produced by CoolParser#Negacao.
    def exitNegacao(self, ctx:CoolParser.NegacaoContext):
        pass


    # Enter a parse tree produced by CoolParser#Atribuicao.
    def enterAtribuicao(self, ctx:CoolParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by CoolParser#Atribuicao.
    def exitAtribuicao(self, ctx:CoolParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by CoolParser#ENulo.
    def enterENulo(self, ctx:CoolParser.ENuloContext):
        pass

    # Exit a parse tree produced by CoolParser#ENulo.
    def exitENulo(self, ctx:CoolParser.ENuloContext):
        pass


    # Enter a parse tree produced by CoolParser#Inteiro.
    def enterInteiro(self, ctx:CoolParser.InteiroContext):
        pass

    # Exit a parse tree produced by CoolParser#Inteiro.
    def exitInteiro(self, ctx:CoolParser.InteiroContext):
        pass


    # Enter a parse tree produced by CoolParser#Loop.
    def enterLoop(self, ctx:CoolParser.LoopContext):
        pass

    # Exit a parse tree produced by CoolParser#Loop.
    def exitLoop(self, ctx:CoolParser.LoopContext):
        pass


    # Enter a parse tree produced by CoolParser#Multiplicacao.
    def enterMultiplicacao(self, ctx:CoolParser.MultiplicacaoContext):
        pass

    # Exit a parse tree produced by CoolParser#Multiplicacao.
    def exitMultiplicacao(self, ctx:CoolParser.MultiplicacaoContext):
        pass


    # Enter a parse tree produced by CoolParser#NovoTipo.
    def enterNovoTipo(self, ctx:CoolParser.NovoTipoContext):
        pass

    # Exit a parse tree produced by CoolParser#NovoTipo.
    def exitNovoTipo(self, ctx:CoolParser.NovoTipoContext):
        pass


    # Enter a parse tree produced by CoolParser#ExprArroba.
    def enterExprArroba(self, ctx:CoolParser.ExprArrobaContext):
        pass

    # Exit a parse tree produced by CoolParser#ExprArroba.
    def exitExprArroba(self, ctx:CoolParser.ExprArrobaContext):
        pass


    # Enter a parse tree produced by CoolParser#Menor.
    def enterMenor(self, ctx:CoolParser.MenorContext):
        pass

    # Exit a parse tree produced by CoolParser#Menor.
    def exitMenor(self, ctx:CoolParser.MenorContext):
        pass


    # Enter a parse tree produced by CoolParser#Let.
    def enterLet(self, ctx:CoolParser.LetContext):
        pass

    # Exit a parse tree produced by CoolParser#Let.
    def exitLet(self, ctx:CoolParser.LetContext):
        pass


    # Enter a parse tree produced by CoolParser#Identificador.
    def enterIdentificador(self, ctx:CoolParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by CoolParser#Identificador.
    def exitIdentificador(self, ctx:CoolParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by CoolParser#If.
    def enterIf(self, ctx:CoolParser.IfContext):
        pass

    # Exit a parse tree produced by CoolParser#If.
    def exitIf(self, ctx:CoolParser.IfContext):
        pass


    # Enter a parse tree produced by CoolParser#ExprParenteses.
    def enterExprParenteses(self, ctx:CoolParser.ExprParentesesContext):
        pass

    # Exit a parse tree produced by CoolParser#ExprParenteses.
    def exitExprParenteses(self, ctx:CoolParser.ExprParentesesContext):
        pass



del CoolParser