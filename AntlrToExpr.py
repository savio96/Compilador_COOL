from string import String_
from CoolParser import CoolParser
from CoolVisitor import CoolVisitor
from antlr4 import *
import re
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
from exprArroba import *
from variasExpressoes import *
from number import *
from let import *


class AntlrToExpr(CoolVisitor):

    def __init__(self, erro, metodo, variavel, tipo, geraCodigo, metodosCool, topoArq, qtdParam, outMain,atributoClasse,
                 numReg,thisReg,herancaOO,classe):
        super().__init__()
        self.variavel = variavel
        self.tipos = []
        self.metodo = metodo
        self.erros_semanticos = erro
        self.tipo = tipo
        self.geraCodigo = geraCodigo
        self.metodosCool = metodosCool
        self.topoArq = topoArq
        self.qtdParam = qtdParam
        self.outMain = outMain
        self.atributoClasse=atributoClasse
        self.numReg=numReg
        self.thisReg=thisReg
        self.herancaOO=herancaOO
        self.classe=classe

    def visitDeclaracaoFormal(self, ctx: CoolParser.DeclaracaoFormalContext):
        id = ctx.getChild(0).getText()
        tipo = ctx.getChild(2).getText()
        if tipo not in self.tipo:
            self.erros_semanticos.append("Tipo nao existe " + tipo)
        if id in self.variavel:
            self.erros_semanticos.append("Variavel " + id + " ja declarada!!")
        else:
            self.variavel[id] = [tipo, "none"]
        #geração de código
        d = DeclaracaoFormal(id, tipo)
        linha = d.mostrar()
        self.geraCodigo.append(linha)
        return DeclaracaoFormal(id, tipo)

    def visitMenorIgual(self, ctx: CoolParser.MenorIgualContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        esq = exprVisitor.visit(ctx.getChild(0))
        dir = exprVisitor.visit(ctx.getChild(2))
        # geração de código
        m=MenorIgual(esq,dir,self.numReg)
        linha,var=m.mostrar()
        for x in linha:
            self.geraCodigo.append(x)
        return var



    def visitVariasExpr(self, ctx: CoolParser.VariasExprContext):
        variasExpr = []
        listaFinal = []
        listaFinalCool = []

        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        id = ctx.getChild(0).getText()
        variasExpr.append(id)

        for i in range(2, ctx.getChildCount() - 1):
            if ctx.getChild(i).getText() != ",":
                var = exprVisitor.visit(ctx.getChild(i))
                variasExpr.append(var)

        for lista in self.metodo.values():
            listaFinal += lista
        for listaCool in self.metodosCool.values():
            listaFinalCool += listaCool
        listaFinalCool = str(listaFinalCool).replace("[", "").replace("]", "")

        l = str(self.outMain)
        listaFinal = str(listaFinal).replace("[", "").replace("]", "")

        if id not in listaFinal:
            self.erros_semanticos.append("Metodo " + id + " não existe")

        elif id in listaFinalCool and id not in l:
            expVar = VariasExpressoes(id, self.metodosCool)
            if id == "out_int":
                var2 = expVar.insereMetodo()
                self.topoArq.append(var2)

        # geração de código
        muitasExp = VariasExpressoes(id, self.metodosCool)
        linha = muitasExp.mostrar(var)
        self.geraCodigo.append(linha)
        return VariasExpressoes(id, self.metodosCool)

    def visitNegacaoNot(self, ctx: CoolParser.NegacaoNotContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        var = exprVisitor.visit(ctx.getChild(1))
        return NegacaoNot(var)

    def visitFalso(self, ctx: CoolParser.FalsoContext):
        return False

    def visitString(self, ctx: CoolParser.StringContext):
        str = ctx.getChild(0).getText()
        return String_(str)

    def visitSubtracao(self, ctx: CoolParser.SubtracaoContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        esq = exprVisitor.visit(ctx.getChild(0))
        dir = exprVisitor.visit(ctx.getChild(2))
        # geração de código
        s = Subtracao(esq, dir, self.numReg)
        vet, str = Subtracao.mostrar(s)
        for i in vet:
            self.geraCodigo.append(i)
        return str

    def visitDivisao(self, ctx: CoolParser.DivisaoContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        esq = exprVisitor.visit(ctx.getChild(0))
        dir = exprVisitor.visit(ctx.getChild(2))
        # geração de código
        d = Divisao(esq, dir, self.numReg)
        vet, str = Divisao.mostrar(d)
        for i in vet:
            self.geraCodigo.append(i)
        return str

    def visitCase(self, ctx: CoolParser.CaseContext):
        return super().visitCase(ctx)

    def visitVerdadeiro(self, ctx: CoolParser.VerdadeiroContext):
        return True

    def visitAdicao(self, ctx: CoolParser.AdicaoContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        esq = exprVisitor.visit(ctx.getChild(0))
        dir = exprVisitor.visit(ctx.getChild(2))

        tipoRetorno=[]
        for x in self.variavel.keys():
            if self.variavel.get(x)[1]==esq:
                tipoRetorno.append(self.variavel.get(x)[0])
        # geração de código
        s = Soma(esq, dir,self.numReg)
        vet, str = Soma.mostrar(s)
        self.variavel[str]=[tipoRetorno[0],"none"]
        for i in vet:
            self.geraCodigo.append(i)
        return str

    def visitIgual(self, ctx: CoolParser.IgualContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        esq = exprVisitor.visit(ctx.getChild(0))
        dir = exprVisitor.visit(ctx.getChild(2))
        # geração de código
        i = Igual(esq, dir, self.numReg)
        linha, var = i.mostrar()
        for x in linha:
            self.geraCodigo.append(x)
        return var

    def visitExprChaves(self, ctx: CoolParser.ExprChavesContext):
        expr = []
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)

        for i in range(1, ctx.getChildCount() - 1):
            if ctx.getChild(i).getText() != ";":
                var = exprVisitor.visit(ctx.getChild(i))
                expr.append(var)
        return ExprChaves(expr)

    def visitNegacao(self, ctx: CoolParser.NegacaoContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        var = exprVisitor.visit(ctx.getChild(1))
        return Negacao(var)

    def visitAtribuicao(self, ctx: CoolParser.AtribuicaoContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        esq = ctx.getChild(0).getText()
        dir = exprVisitor.visit(ctx.getChild(2))
        dir2 = ctx.getChild(2).getText()
        try:
            dir2=int(dir2)
        except:
            pass
        valor = dir
        tipoDir = ""
        if esq not in self.variavel:
            self.erros_semanticos.append("Variavel " + esq + " nao declarada!!")
        else:
            for id in self.variavel.keys():
                if id == esq:
                    tipoVar = self.variavel[id][0]
                    texto = str(type(dir2))
                    if texto == "<class 'int'>":
                        tipoDir = 'Int'
                    elif texto=="<class 'str'>":
                        if dir2 not in self.variavel:
                            self.erros_semanticos.append("Variavel " + dir2 + " nao declarada!!")
                        else:
                            tipoDir=self.variavel[dir2][0]
                    if tipoVar == tipoDir:
                        self.variavel[id][1] = valor

                    else:
                        self.erros_semanticos.append(
                            "Tipos incompatíveis: variável " + id + " do tipo " + tipoVar + " recebendo valor da variavel "
                            + dir + " do tipo " + tipoDir)

        # geração de código
        atri=Atribuicao(esq,valor,self.atributoClasse,self.thisReg)

        self.geraCodigo.append(atri.mostrar())

        return Atribuicao(esq, valor,self.atributoClasse,self.thisReg)

    def visitENulo(self, ctx: CoolParser.ENuloContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        var = exprVisitor.visit(ctx.getChild(1))
        return Enulo(var)

    def visitInteiro(self, ctx: CoolParser.InteiroContext):
        numText = ctx.getChild(0).getText()
        num = Number(numText,self.numReg)
        inteiro, var = num.mostrar()
        # geração de código
        self.geraCodigo.append(inteiro)
        return var

    def visitLoop(self, ctx: CoolParser.LoopContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        esq = exprVisitor.visit(ctx.getChild(1))
        dir = exprVisitor.visit(ctx.getChild(3))
        # geração de código
        lo=Loop(esq,dir,self.numReg)
        linha,var=lo.mostrar()
        for x in linha:
            self.geraCodigo.append(x)
        return var

    def visitMultiplicacao(self, ctx: CoolParser.MultiplicacaoContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        esq = exprVisitor.visit(ctx.getChild(0))
        dir = exprVisitor.visit(ctx.getChild(2))
        # geração de código
        mul=Multiplication(esq,dir,self.numReg)
        linha,var=mul.mostrar()
        for x in linha:
            self.geraCodigo.append(x)
        return var

    def visitNovoTipo(self, ctx: CoolParser.NovoTipoContext):
        var = ctx.getChild(1).getText()
        if var not in self.tipo:
            self.tipo.append(var)
        else:
            self.erros_semanticos.append("Tipo já declarado " + var)
        return super().visitNovoTipo(ctx)

    def visitExprArroba(self, ctx: CoolParser.ExprArrobaContext):
        listaFinal = []
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        id = exprVisitor.visit(ctx.ID())
        for lista in self.metodo.values():
            listaFinal += lista

        if id not in listaFinal:
            self.erros_semanticos.append("Metodo " + id + " não existe")
        elif id in self.metodosCool:
            # geração de código
            expAr = ExprArroba(id, self.metodosCool)
            geraColocar = expAr.mostrar()
            self.geraCodigo.append(geraColocar)

        return ExprArroba(id, self.metodosCool)

    def visitMenor(self, ctx: CoolParser.MenorContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        esq = exprVisitor.visit(ctx.getChild(0))
        dir = exprVisitor.visit(ctx.getChild(2))
        # geração de código
        m=Menor(esq,dir,self.numReg)
        linha,str=m.mostrar()
        for x in linha:
            self.geraCodigo.append(x)
        return str

    def visitLet(self, ctx: CoolParser.LetContext):
        letVisitor= AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain, self.atributoClasse,
                                  self.numReg, self.thisReg, self.herancaOO,self.classe)
        id = ctx.getChild(1).getText()
        tipo=ctx.getChild(3).getText()
        valor=ctx.getChild(5).getText()
        if tipo not in self.tipo:
            self.erros_semanticos.append("Tipo nao existe " + tipo)
        if id in self.variavel:
            self.erros_semanticos.append("Variavel " + id + " ja declarada!!")
        else:
            if ctx.getChildCount() <6:
                dir2 = "none"
                valor = "none"
                self.variavel[id] = [tipo, valor]

                if self.classe not in self.atributoClasse.keys():
                    self.atributoClasse[self.classe]=[[id]]
                else:
                    self.atributoClasse[self.classe][0].append(id)
            dir2 = ctx.getChild(5).getText()
        # geração de código
        linha=Let(id,tipo,valor,self.variavel)
        linha.mostrar()
        return Let(id,tipo,valor,self.variavel)

    def visitIdentificador(self, ctx: CoolParser.IdentificadorContext):
        id = ctx.getChild(0).getText()
        if id not in self.variavel and id!="self":
            self.erros_semanticos.append("variavel " + id + " nao declarada!!")
        # geração de código
        var=Variable(id,self.atributoClasse,self.numReg,self.thisReg,self.variavel)
        linha,reg=var.mostrar()
        self.geraCodigo.append(linha)
        return reg

    def visitIf(self, ctx: CoolParser.IfContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        esq = exprVisitor.visit(ctx.getChild(1))
        meio = exprVisitor.visit(ctx.getChild(3))
        dir = exprVisitor.visit(ctx.getChild(5))
        # geração de código
        i=IfCon(esq,meio,dir,self.numReg)
        linha,str1,str2=i.mostrar()
        for x in linha:
            self.geraCodigo.append(x)
        return str1,str2

    def visitExprParenteses(self, ctx: CoolParser.ExprParentesesContext):
        exprVisitor = AntlrToExpr(self.erros_semanticos, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodosCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        var = exprVisitor.visit(ctx.getChild(1))
        return ExprParenteses(var)
