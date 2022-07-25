from CoolParser import CoolParser
from CoolVisitor import CoolVisitor
from feature import *
from AntlrToExpr import *
from AntlrToClass import *


class AntlrToFeature(CoolVisitor):
    def __init__(self, erro, metodo, variavel, tipo, classe,geraCodigo,metodosCool,outMain,qtdParam,atributoClasse,
                 numReg,thisReg,herancaOO):
        super().__init__()
        self.erroSemantico = erro
        self.metodo = metodo
        self.variavel = variavel
        self.tipo = tipo
        self.classe=classe
        self.geraCodigo=[]
        self.geraCodigoClasse=geraCodigo
        self.metodoCool=metodosCool
        self.topoArq=[]
        self.qtdParam=qtdParam
        self.qtdParam["out_int"]=[1]
        self.outMain=outMain
        self.atributoClasse=atributoClasse
        self.numReg=numReg
        self.thisReg=thisReg
        self.herancaOO=herancaOO

    def visitMetodo(self, ctx: CoolParser.MetodoContext):
        listaFinal=[]
        if (ctx.getChildCount()==8):
            qtd=0
        else:
            qtd = (ctx.getChildCount() - 8 + 1) / 2
        feature = Feature()
        me = ctx.ID().getText()
        id = self.classe
        var = ctx.TYPE().getText()
        if var not in self.tipo:
            self.erroSemantico.append("Tipo nao existe " + var)

        for lista in self.metodo.values():
            listaFinal += lista

        if me not in listaFinal:
            if id not in self.metodo.keys():
                self.metodo[id] = [[me]]
            else:
                self.metodo[id][0].append(me)
            self.qtdParam[me] = [qtd]
        else:
            self.erroSemantico.append("Metodo " + me + " já existe")

        # geração de código
        if me == "main" and id == "Main":
            linha = "@main {"
        else:
            linha = '@' + me + '_' + id + '(this: ptr<int>'

        exprVisitor = AntlrToExpr(self.erroSemantico, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodoCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
        # geração de código
        for i in range(0, ctx.getChildCount()):
            if i != ctx.getChildCount() - 1:
                feature.adicionarExpr(exprVisitor.visit(ctx.getChild(i)))
                if ctx.getChild(i+1).getText()==")" and id!="Main":
                    self.geraCodigo.append("):")
                elif ctx.getChild(i).getText()==":" and id!="Main":
                    if ctx.getChild(i+1).getText()=="Int":
                        lin="int {"
                    else:
                        lin="ptr<int> {"
                    self.geraCodigo.append(lin)

        self.geraCodigo.insert(0,linha)
        if me != "main" and id != "Main":
            self.geraCodigo.append("ret this;")
        self.geraCodigo.append("}")
        self.geraCodigoClasse.extend(self.geraCodigo)
        if len(self.topoArq)!=0:
            self.geraCodigoClasse.insert(0, self.topoArq[0])
        self.geraCodigo=[]
        return feature

    def visitDeclaracaoFeature(self, ctx: CoolParser.DeclaracaoFeatureContext):
        feature = Feature()
        exprVisitor = AntlrToExpr(self.erroSemantico, self.metodo, self.variavel, self.tipo, self.geraCodigo,
                                  self.metodoCool, self.topoArq, self.qtdParam, self.outMain,self.atributoClasse,
                                  self.numReg,self.thisReg,self.herancaOO,self.classe)
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

                if self.classe not in self.atributoClasse.keys():
                    self.atributoClasse[self.classe]=[[id]]
                else:
                    self.atributoClasse[self.classe][0].append(id)

            else:
                valor = exprVisitor.visit(ctx.getChild(4))
                dir2 = ctx.getChild(4).getText()
                tipoDir="none"
                texto = str(type(valor))
                #print(texto)
                try:
                    dir2 = int(dir2)
                except:
                    pass
                texto = str(type(dir2))
                # print(texto)
                if texto == "<class 'int'>":
                    tipoDir = 'Int'
                elif texto == "<class 'str'>":
                    tipoDir = 'String'

                if tipo == tipoDir:
                    self.variavel[id] = [tipo, valor]
                    if self.classe not in self.atributoClasse.keys():
                        self.atributoClasse[self.classe] = [[id]]
                    else:
                        self.atributoClasse[self.classe][0].append(id)

                else:
                    self.erroSemantico.append("Tipos incompatíveis: variável " + id + " do tipo " + tipo + " recebendo valor do tipo " + tipoDir)
        return feature
