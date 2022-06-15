# Generated from Cool.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,213,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,1,1,1,1,3,1,24,8,1,1,1,1,1,
        1,1,1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        5,2,42,8,2,10,2,12,2,45,9,2,3,2,47,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,61,8,2,3,2,63,8,2,1,3,1,3,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,78,8,4,10,4,12,4,81,9,4,3,4,
        83,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,4,4,104,8,4,11,4,12,4,105,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,3,4,116,8,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,124,8,4,5,4,
        126,8,4,10,4,12,4,129,9,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,4,4,143,8,4,11,4,12,4,144,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,166,8,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,192,8,4,1,4,1,4,1,4,1,4,1,4,1,4,
        5,4,200,8,4,10,4,12,4,203,9,4,3,4,205,8,4,1,4,5,4,208,8,4,10,4,12,
        4,211,9,4,1,4,0,1,8,5,0,2,4,6,8,0,0,248,0,13,1,0,0,0,2,19,1,0,0,
        0,4,62,1,0,0,0,6,64,1,0,0,0,8,165,1,0,0,0,10,11,3,2,1,0,11,12,5,
        1,0,0,12,14,1,0,0,0,13,10,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,
        16,1,0,0,0,16,17,1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,20,5,2,0,
        0,20,23,5,40,0,0,21,22,5,3,0,0,22,24,5,40,0,0,23,21,1,0,0,0,23,24,
        1,0,0,0,24,25,1,0,0,0,25,31,5,4,0,0,26,27,3,4,2,0,27,28,5,1,0,0,
        28,30,1,0,0,0,29,26,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,
        0,0,0,32,34,1,0,0,0,33,31,1,0,0,0,34,35,5,5,0,0,35,3,1,0,0,0,36,
        37,5,39,0,0,37,46,5,6,0,0,38,43,3,6,3,0,39,40,5,7,0,0,40,42,3,6,
        3,0,41,39,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,47,
        1,0,0,0,45,43,1,0,0,0,46,38,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,
        48,49,5,8,0,0,49,50,5,9,0,0,50,51,5,40,0,0,51,52,5,4,0,0,52,53,3,
        8,4,0,53,54,5,5,0,0,54,63,1,0,0,0,55,56,5,39,0,0,56,57,5,9,0,0,57,
        60,5,40,0,0,58,59,5,10,0,0,59,61,3,8,4,0,60,58,1,0,0,0,60,61,1,0,
        0,0,61,63,1,0,0,0,62,36,1,0,0,0,62,55,1,0,0,0,63,5,1,0,0,0,64,65,
        5,39,0,0,65,66,5,9,0,0,66,67,5,40,0,0,67,7,1,0,0,0,68,69,6,4,-1,
        0,69,70,5,39,0,0,70,71,5,10,0,0,71,166,3,8,4,25,72,73,5,39,0,0,73,
        82,5,6,0,0,74,79,3,8,4,0,75,76,5,7,0,0,76,78,3,8,4,0,77,75,1,0,0,
        0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,83,1,0,0,0,81,79,
        1,0,0,0,82,74,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,166,5,8,0,0,
        85,86,5,13,0,0,86,87,3,8,4,0,87,88,5,14,0,0,88,89,3,8,4,0,89,90,
        5,15,0,0,90,91,3,8,4,0,91,92,5,16,0,0,92,166,1,0,0,0,93,94,5,17,
        0,0,94,95,3,8,4,0,95,96,5,18,0,0,96,97,3,8,4,0,97,98,5,19,0,0,98,
        166,1,0,0,0,99,103,5,4,0,0,100,101,3,8,4,0,101,102,5,1,0,0,102,104,
        1,0,0,0,103,100,1,0,0,0,104,105,1,0,0,0,105,103,1,0,0,0,105,106,
        1,0,0,0,106,107,1,0,0,0,107,108,5,5,0,0,108,166,1,0,0,0,109,110,
        5,20,0,0,110,111,5,39,0,0,111,112,5,9,0,0,112,115,5,40,0,0,113,114,
        5,10,0,0,114,116,3,8,4,0,115,113,1,0,0,0,115,116,1,0,0,0,116,127,
        1,0,0,0,117,118,5,7,0,0,118,119,5,39,0,0,119,120,5,9,0,0,120,123,
        5,40,0,0,121,122,5,10,0,0,122,124,3,8,4,0,123,121,1,0,0,0,123,124,
        1,0,0,0,124,126,1,0,0,0,125,117,1,0,0,0,126,129,1,0,0,0,127,125,
        1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,127,1,0,0,0,130,131,
        5,21,0,0,131,166,3,8,4,19,132,133,5,22,0,0,133,134,3,8,4,0,134,142,
        5,23,0,0,135,136,5,39,0,0,136,137,5,9,0,0,137,138,5,40,0,0,138,139,
        5,24,0,0,139,140,3,8,4,0,140,141,5,1,0,0,141,143,1,0,0,0,142,135,
        1,0,0,0,143,144,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,146,
        1,0,0,0,146,147,5,25,0,0,147,166,1,0,0,0,148,149,5,26,0,0,149,166,
        5,40,0,0,150,151,5,27,0,0,151,166,3,8,4,16,152,153,5,32,0,0,153,
        166,3,8,4,11,154,155,5,36,0,0,155,166,3,8,4,7,156,157,5,6,0,0,157,
        158,3,8,4,0,158,159,5,8,0,0,159,166,1,0,0,0,160,166,5,39,0,0,161,
        166,5,42,0,0,162,166,5,41,0,0,163,166,5,37,0,0,164,166,5,38,0,0,
        165,68,1,0,0,0,165,72,1,0,0,0,165,85,1,0,0,0,165,93,1,0,0,0,165,
        99,1,0,0,0,165,109,1,0,0,0,165,132,1,0,0,0,165,148,1,0,0,0,165,150,
        1,0,0,0,165,152,1,0,0,0,165,154,1,0,0,0,165,156,1,0,0,0,165,160,
        1,0,0,0,165,161,1,0,0,0,165,162,1,0,0,0,165,163,1,0,0,0,165,164,
        1,0,0,0,166,209,1,0,0,0,167,168,10,15,0,0,168,169,5,28,0,0,169,208,
        3,8,4,16,170,171,10,14,0,0,171,172,5,29,0,0,172,208,3,8,4,15,173,
        174,10,13,0,0,174,175,5,30,0,0,175,208,3,8,4,14,176,177,10,12,0,
        0,177,178,5,31,0,0,178,208,3,8,4,13,179,180,10,10,0,0,180,181,5,
        33,0,0,181,208,3,8,4,11,182,183,10,9,0,0,183,184,5,34,0,0,184,208,
        3,8,4,10,185,186,10,8,0,0,186,187,5,35,0,0,187,208,3,8,4,9,188,191,
        10,24,0,0,189,190,5,11,0,0,190,192,5,40,0,0,191,189,1,0,0,0,191,
        192,1,0,0,0,192,193,1,0,0,0,193,194,5,12,0,0,194,195,5,39,0,0,195,
        204,5,6,0,0,196,201,3,8,4,0,197,198,5,7,0,0,198,200,3,8,4,0,199,
        197,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,
        205,1,0,0,0,203,201,1,0,0,0,204,196,1,0,0,0,204,205,1,0,0,0,205,
        206,1,0,0,0,206,208,5,8,0,0,207,167,1,0,0,0,207,170,1,0,0,0,207,
        173,1,0,0,0,207,176,1,0,0,0,207,179,1,0,0,0,207,182,1,0,0,0,207,
        185,1,0,0,0,207,188,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,
        210,1,0,0,0,210,9,1,0,0,0,211,209,1,0,0,0,20,15,23,31,43,46,60,62,
        79,82,105,115,123,127,144,165,191,201,204,207,209
    ]

class CoolParser ( Parser ):

    grammarFileName = "Cool.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'class'", "'inherits'", "'{'", 
                     "'}'", "'('", "','", "')'", "':'", "'<-'", "'@'", "'.'", 
                     "'if'", "'then'", "'else'", "'fi'", "'while'", "'loop'", 
                     "'pool'", "'let'", "'in'", "'case'", "'of'", "'=>'", 
                     "'esac'", "'new'", "'isvoid'", "'+'", "'-'", "'*'", 
                     "'/'", "'~'", "'<'", "'<='", "'='", "'not'", "'true'", 
                     "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "TYPE", 
                      "STRING", "INTEGER", "WS", "LINE_COMMENT", "COMMENT" ]

    RULE_prog = 0
    RULE_class = 1
    RULE_feature = 2
    RULE_formal = 3
    RULE_expr = 4

    ruleNames =  [ "prog", "class", "feature", "formal", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    ID=39
    TYPE=40
    STRING=41
    INTEGER=42
    WS=43
    LINE_COMMENT=44
    COMMENT=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CoolParser.RULE_prog

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramaContext(ProgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ProgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(CoolParser.EOF, 0)
        def class_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ClassContext)
            else:
                return self.getTypedRuleContext(CoolParser.ClassContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)



    def prog(self):

        localctx = CoolParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            localctx = CoolParser.ProgramaContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.class_()
                self.state = 11
                self.match(CoolParser.T__0)
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CoolParser.T__1):
                    break

            self.state = 17
            self.match(CoolParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CoolParser.RULE_class

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ClasseContext(ClassContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ClassContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(CoolParser.TYPE)
            else:
                return self.getToken(CoolParser.TYPE, i)
        def feature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.FeatureContext)
            else:
                return self.getTypedRuleContext(CoolParser.FeatureContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClasse" ):
                listener.enterClasse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClasse" ):
                listener.exitClasse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasse" ):
                return visitor.visitClasse(self)
            else:
                return visitor.visitChildren(self)



    def class_(self):

        localctx = CoolParser.ClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class)
        self._la = 0 # Token type
        try:
            localctx = CoolParser.ClasseContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(CoolParser.T__1)
            self.state = 20
            self.match(CoolParser.TYPE)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CoolParser.T__2:
                self.state = 21
                self.match(CoolParser.T__2)
                self.state = 22
                self.match(CoolParser.TYPE)


            self.state = 25
            self.match(CoolParser.T__3)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CoolParser.ID:
                self.state = 26
                self.feature()
                self.state = 27
                self.match(CoolParser.T__0)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(CoolParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CoolParser.RULE_feature

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MetodoContext(FeatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.FeatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CoolParser.ID, 0)
        def TYPE(self):
            return self.getToken(CoolParser.TYPE, 0)
        def expr(self):
            return self.getTypedRuleContext(CoolParser.ExprContext,0)

        def formal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.FormalContext)
            else:
                return self.getTypedRuleContext(CoolParser.FormalContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetodo" ):
                listener.enterMetodo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetodo" ):
                listener.exitMetodo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetodo" ):
                return visitor.visitMetodo(self)
            else:
                return visitor.visitChildren(self)


    class DeclaracaoFeatureContext(FeatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.FeatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CoolParser.ID, 0)
        def TYPE(self):
            return self.getToken(CoolParser.TYPE, 0)
        def expr(self):
            return self.getTypedRuleContext(CoolParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoFeature" ):
                listener.enterDeclaracaoFeature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoFeature" ):
                listener.exitDeclaracaoFeature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracaoFeature" ):
                return visitor.visitDeclaracaoFeature(self)
            else:
                return visitor.visitChildren(self)



    def feature(self):

        localctx = CoolParser.FeatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_feature)
        self._la = 0 # Token type
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = CoolParser.MetodoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(CoolParser.ID)
                self.state = 37
                self.match(CoolParser.T__5)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CoolParser.ID:
                    self.state = 38
                    self.formal()
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CoolParser.T__6:
                        self.state = 39
                        self.match(CoolParser.T__6)
                        self.state = 40
                        self.formal()
                        self.state = 45
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 48
                self.match(CoolParser.T__7)
                self.state = 49
                self.match(CoolParser.T__8)
                self.state = 50
                self.match(CoolParser.TYPE)
                self.state = 51
                self.match(CoolParser.T__3)
                self.state = 52
                self.expr(0)
                self.state = 53
                self.match(CoolParser.T__4)
                pass

            elif la_ == 2:
                localctx = CoolParser.DeclaracaoFeatureContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(CoolParser.ID)
                self.state = 56
                self.match(CoolParser.T__8)
                self.state = 57
                self.match(CoolParser.TYPE)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CoolParser.T__9:
                    self.state = 58
                    self.match(CoolParser.T__9)
                    self.state = 59
                    self.expr(0)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CoolParser.RULE_formal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclaracaoFormalContext(FormalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.FormalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CoolParser.ID, 0)
        def TYPE(self):
            return self.getToken(CoolParser.TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoFormal" ):
                listener.enterDeclaracaoFormal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoFormal" ):
                listener.exitDeclaracaoFormal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracaoFormal" ):
                return visitor.visitDeclaracaoFormal(self)
            else:
                return visitor.visitChildren(self)



    def formal(self):

        localctx = CoolParser.FormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_formal)
        try:
            localctx = CoolParser.DeclaracaoFormalContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(CoolParser.ID)
            self.state = 65
            self.match(CoolParser.T__8)
            self.state = 66
            self.match(CoolParser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CoolParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MenorIgualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ExprContext)
            else:
                return self.getTypedRuleContext(CoolParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenorIgual" ):
                listener.enterMenorIgual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenorIgual" ):
                listener.exitMenorIgual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenorIgual" ):
                return visitor.visitMenorIgual(self)
            else:
                return visitor.visitChildren(self)


    class VariasExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CoolParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ExprContext)
            else:
                return self.getTypedRuleContext(CoolParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariasExpr" ):
                listener.enterVariasExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariasExpr" ):
                listener.exitVariasExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariasExpr" ):
                return visitor.visitVariasExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegacaoNotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CoolParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegacaoNot" ):
                listener.enterNegacaoNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegacaoNot" ):
                listener.exitNegacaoNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegacaoNot" ):
                return visitor.visitNegacaoNot(self)
            else:
                return visitor.visitChildren(self)


    class FalsoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalso" ):
                listener.enterFalso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalso" ):
                listener.exitFalso(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalso" ):
                return visitor.visitFalso(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CoolParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class SubtracaoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ExprContext)
            else:
                return self.getTypedRuleContext(CoolParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtracao" ):
                listener.enterSubtracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtracao" ):
                listener.exitSubtracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtracao" ):
                return visitor.visitSubtracao(self)
            else:
                return visitor.visitChildren(self)


    class DivisaoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ExprContext)
            else:
                return self.getTypedRuleContext(CoolParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivisao" ):
                listener.enterDivisao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivisao" ):
                listener.exitDivisao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivisao" ):
                return visitor.visitDivisao(self)
            else:
                return visitor.visitChildren(self)


    class CaseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ExprContext)
            else:
                return self.getTypedRuleContext(CoolParser.ExprContext,i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CoolParser.ID)
            else:
                return self.getToken(CoolParser.ID, i)
        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(CoolParser.TYPE)
            else:
                return self.getToken(CoolParser.TYPE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase" ):
                listener.enterCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase" ):
                listener.exitCase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCase" ):
                return visitor.visitCase(self)
            else:
                return visitor.visitChildren(self)


    class VerdadeiroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerdadeiro" ):
                listener.enterVerdadeiro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerdadeiro" ):
                listener.exitVerdadeiro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerdadeiro" ):
                return visitor.visitVerdadeiro(self)
            else:
                return visitor.visitChildren(self)


    class AdicaoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ExprContext)
            else:
                return self.getTypedRuleContext(CoolParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdicao" ):
                listener.enterAdicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdicao" ):
                listener.exitAdicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdicao" ):
                return visitor.visitAdicao(self)
            else:
                return visitor.visitChildren(self)


    class IgualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ExprContext)
            else:
                return self.getTypedRuleContext(CoolParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgual" ):
                listener.enterIgual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgual" ):
                listener.exitIgual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgual" ):
                return visitor.visitIgual(self)
            else:
                return visitor.visitChildren(self)


    class ExprChavesContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ExprContext)
            else:
                return self.getTypedRuleContext(CoolParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprChaves" ):
                listener.enterExprChaves(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprChaves" ):
                listener.exitExprChaves(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprChaves" ):
                return visitor.visitExprChaves(self)
            else:
                return visitor.visitChildren(self)


    class NegacaoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CoolParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegacao" ):
                listener.enterNegacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegacao" ):
                listener.exitNegacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegacao" ):
                return visitor.visitNegacao(self)
            else:
                return visitor.visitChildren(self)


    class AtribuicaoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CoolParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(CoolParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)


    class ENuloContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CoolParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterENulo" ):
                listener.enterENulo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitENulo" ):
                listener.exitENulo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitENulo" ):
                return visitor.visitENulo(self)
            else:
                return visitor.visitChildren(self)


    class InteiroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(CoolParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteiro" ):
                listener.enterInteiro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteiro" ):
                listener.exitInteiro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteiro" ):
                return visitor.visitInteiro(self)
            else:
                return visitor.visitChildren(self)


    class LoopContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ExprContext)
            else:
                return self.getTypedRuleContext(CoolParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicacaoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ExprContext)
            else:
                return self.getTypedRuleContext(CoolParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicacao" ):
                listener.enterMultiplicacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicacao" ):
                listener.exitMultiplicacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicacao" ):
                return visitor.visitMultiplicacao(self)
            else:
                return visitor.visitChildren(self)


    class NovoTipoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE(self):
            return self.getToken(CoolParser.TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNovoTipo" ):
                listener.enterNovoTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNovoTipo" ):
                listener.exitNovoTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNovoTipo" ):
                return visitor.visitNovoTipo(self)
            else:
                return visitor.visitChildren(self)


    class ExprArrobaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ExprContext)
            else:
                return self.getTypedRuleContext(CoolParser.ExprContext,i)

        def ID(self):
            return self.getToken(CoolParser.ID, 0)
        def TYPE(self):
            return self.getToken(CoolParser.TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprArroba" ):
                listener.enterExprArroba(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprArroba" ):
                listener.exitExprArroba(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprArroba" ):
                return visitor.visitExprArroba(self)
            else:
                return visitor.visitChildren(self)


    class MenorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ExprContext)
            else:
                return self.getTypedRuleContext(CoolParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenor" ):
                listener.enterMenor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenor" ):
                listener.exitMenor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenor" ):
                return visitor.visitMenor(self)
            else:
                return visitor.visitChildren(self)


    class LetContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CoolParser.ID)
            else:
                return self.getToken(CoolParser.ID, i)
        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(CoolParser.TYPE)
            else:
                return self.getToken(CoolParser.TYPE, i)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ExprContext)
            else:
                return self.getTypedRuleContext(CoolParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet" ):
                listener.enterLet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet" ):
                listener.exitLet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet" ):
                return visitor.visitLet(self)
            else:
                return visitor.visitChildren(self)


    class IdentificadorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CoolParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentificador" ):
                listener.enterIdentificador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentificador" ):
                listener.exitIdentificador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentificador" ):
                return visitor.visitIdentificador(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoolParser.ExprContext)
            else:
                return self.getTypedRuleContext(CoolParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class ExprParentesesContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CoolParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CoolParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprParenteses" ):
                listener.enterExprParenteses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprParenteses" ):
                listener.exitExprParenteses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprParenteses" ):
                return visitor.visitExprParenteses(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CoolParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = CoolParser.AtribuicaoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 69
                self.match(CoolParser.ID)
                self.state = 70
                self.match(CoolParser.T__9)
                self.state = 71
                self.expr(25)
                pass

            elif la_ == 2:
                localctx = CoolParser.VariasExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                self.match(CoolParser.ID)
                self.state = 73
                self.match(CoolParser.T__5)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CoolParser.T__3) | (1 << CoolParser.T__5) | (1 << CoolParser.T__12) | (1 << CoolParser.T__16) | (1 << CoolParser.T__19) | (1 << CoolParser.T__21) | (1 << CoolParser.T__25) | (1 << CoolParser.T__26) | (1 << CoolParser.T__31) | (1 << CoolParser.T__35) | (1 << CoolParser.T__36) | (1 << CoolParser.T__37) | (1 << CoolParser.ID) | (1 << CoolParser.STRING) | (1 << CoolParser.INTEGER))) != 0):
                    self.state = 74
                    self.expr(0)
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CoolParser.T__6:
                        self.state = 75
                        self.match(CoolParser.T__6)
                        self.state = 76
                        self.expr(0)
                        self.state = 81
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 84
                self.match(CoolParser.T__7)
                pass

            elif la_ == 3:
                localctx = CoolParser.IfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 85
                self.match(CoolParser.T__12)
                self.state = 86
                self.expr(0)
                self.state = 87
                self.match(CoolParser.T__13)
                self.state = 88
                self.expr(0)
                self.state = 89
                self.match(CoolParser.T__14)
                self.state = 90
                self.expr(0)
                self.state = 91
                self.match(CoolParser.T__15)
                pass

            elif la_ == 4:
                localctx = CoolParser.LoopContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 93
                self.match(CoolParser.T__16)
                self.state = 94
                self.expr(0)
                self.state = 95
                self.match(CoolParser.T__17)
                self.state = 96
                self.expr(0)
                self.state = 97
                self.match(CoolParser.T__18)
                pass

            elif la_ == 5:
                localctx = CoolParser.ExprChavesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 99
                self.match(CoolParser.T__3)
                self.state = 103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 100
                    self.expr(0)
                    self.state = 101
                    self.match(CoolParser.T__0)
                    self.state = 105 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CoolParser.T__3) | (1 << CoolParser.T__5) | (1 << CoolParser.T__12) | (1 << CoolParser.T__16) | (1 << CoolParser.T__19) | (1 << CoolParser.T__21) | (1 << CoolParser.T__25) | (1 << CoolParser.T__26) | (1 << CoolParser.T__31) | (1 << CoolParser.T__35) | (1 << CoolParser.T__36) | (1 << CoolParser.T__37) | (1 << CoolParser.ID) | (1 << CoolParser.STRING) | (1 << CoolParser.INTEGER))) != 0)):
                        break

                self.state = 107
                self.match(CoolParser.T__4)
                pass

            elif la_ == 6:
                localctx = CoolParser.LetContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                self.match(CoolParser.T__19)
                self.state = 110
                self.match(CoolParser.ID)
                self.state = 111
                self.match(CoolParser.T__8)
                self.state = 112
                self.match(CoolParser.TYPE)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CoolParser.T__9:
                    self.state = 113
                    self.match(CoolParser.T__9)
                    self.state = 114
                    self.expr(0)


                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CoolParser.T__6:
                    self.state = 117
                    self.match(CoolParser.T__6)
                    self.state = 118
                    self.match(CoolParser.ID)
                    self.state = 119
                    self.match(CoolParser.T__8)
                    self.state = 120
                    self.match(CoolParser.TYPE)
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==CoolParser.T__9:
                        self.state = 121
                        self.match(CoolParser.T__9)
                        self.state = 122
                        self.expr(0)


                    self.state = 129
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 130
                self.match(CoolParser.T__20)
                self.state = 131
                self.expr(19)
                pass

            elif la_ == 7:
                localctx = CoolParser.CaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 132
                self.match(CoolParser.T__21)
                self.state = 133
                self.expr(0)
                self.state = 134
                self.match(CoolParser.T__22)
                self.state = 142 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 135
                    self.match(CoolParser.ID)
                    self.state = 136
                    self.match(CoolParser.T__8)
                    self.state = 137
                    self.match(CoolParser.TYPE)
                    self.state = 138
                    self.match(CoolParser.T__23)
                    self.state = 139
                    self.expr(0)
                    self.state = 140
                    self.match(CoolParser.T__0)
                    self.state = 144 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==CoolParser.ID):
                        break

                self.state = 146
                self.match(CoolParser.T__24)
                pass

            elif la_ == 8:
                localctx = CoolParser.NovoTipoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(CoolParser.T__25)
                self.state = 149
                self.match(CoolParser.TYPE)
                pass

            elif la_ == 9:
                localctx = CoolParser.ENuloContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.match(CoolParser.T__26)
                self.state = 151
                self.expr(16)
                pass

            elif la_ == 10:
                localctx = CoolParser.NegacaoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 152
                self.match(CoolParser.T__31)
                self.state = 153
                self.expr(11)
                pass

            elif la_ == 11:
                localctx = CoolParser.NegacaoNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 154
                self.match(CoolParser.T__35)
                self.state = 155
                self.expr(7)
                pass

            elif la_ == 12:
                localctx = CoolParser.ExprParentesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 156
                self.match(CoolParser.T__5)
                self.state = 157
                self.expr(0)
                self.state = 158
                self.match(CoolParser.T__7)
                pass

            elif la_ == 13:
                localctx = CoolParser.IdentificadorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 160
                self.match(CoolParser.ID)
                pass

            elif la_ == 14:
                localctx = CoolParser.InteiroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 161
                self.match(CoolParser.INTEGER)
                pass

            elif la_ == 15:
                localctx = CoolParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 162
                self.match(CoolParser.STRING)
                pass

            elif la_ == 16:
                localctx = CoolParser.VerdadeiroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 163
                self.match(CoolParser.T__36)
                pass

            elif la_ == 17:
                localctx = CoolParser.FalsoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 164
                self.match(CoolParser.T__37)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 207
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = CoolParser.AdicaoContext(self, CoolParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 167
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 168
                        self.match(CoolParser.T__27)
                        self.state = 169
                        self.expr(16)
                        pass

                    elif la_ == 2:
                        localctx = CoolParser.SubtracaoContext(self, CoolParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 170
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 171
                        self.match(CoolParser.T__28)
                        self.state = 172
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = CoolParser.MultiplicacaoContext(self, CoolParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 173
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 174
                        self.match(CoolParser.T__29)
                        self.state = 175
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = CoolParser.DivisaoContext(self, CoolParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 176
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 177
                        self.match(CoolParser.T__30)
                        self.state = 178
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = CoolParser.MenorContext(self, CoolParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 179
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 180
                        self.match(CoolParser.T__32)
                        self.state = 181
                        self.expr(11)
                        pass

                    elif la_ == 6:
                        localctx = CoolParser.MenorIgualContext(self, CoolParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 182
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 183
                        self.match(CoolParser.T__33)
                        self.state = 184
                        self.expr(10)
                        pass

                    elif la_ == 7:
                        localctx = CoolParser.IgualContext(self, CoolParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 185
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 186
                        self.match(CoolParser.T__34)
                        self.state = 187
                        self.expr(9)
                        pass

                    elif la_ == 8:
                        localctx = CoolParser.ExprArrobaContext(self, CoolParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 188
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 191
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==CoolParser.T__10:
                            self.state = 189
                            self.match(CoolParser.T__10)
                            self.state = 190
                            self.match(CoolParser.TYPE)


                        self.state = 193
                        self.match(CoolParser.T__11)
                        self.state = 194
                        self.match(CoolParser.ID)
                        self.state = 195
                        self.match(CoolParser.T__5)
                        self.state = 204
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CoolParser.T__3) | (1 << CoolParser.T__5) | (1 << CoolParser.T__12) | (1 << CoolParser.T__16) | (1 << CoolParser.T__19) | (1 << CoolParser.T__21) | (1 << CoolParser.T__25) | (1 << CoolParser.T__26) | (1 << CoolParser.T__31) | (1 << CoolParser.T__35) | (1 << CoolParser.T__36) | (1 << CoolParser.T__37) | (1 << CoolParser.ID) | (1 << CoolParser.STRING) | (1 << CoolParser.INTEGER))) != 0):
                            self.state = 196
                            self.expr(0)
                            self.state = 201
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==CoolParser.T__6:
                                self.state = 197
                                self.match(CoolParser.T__6)
                                self.state = 198
                                self.expr(0)
                                self.state = 203
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 206
                        self.match(CoolParser.T__7)
                        pass

             
                self.state = 211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 24)
         




