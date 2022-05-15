# Generated from Cool.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CoolParser import CoolParser
else:
    from CoolParser import CoolParser

# This class defines a complete listener for a parse tree produced by CoolParser.
class CoolListener(ParseTreeListener):

    # Enter a parse tree produced by CoolParser#prog.
    def enterProg(self, ctx:CoolParser.ProgContext):
        pass

    # Exit a parse tree produced by CoolParser#prog.
    def exitProg(self, ctx:CoolParser.ProgContext):
        pass


    # Enter a parse tree produced by CoolParser#class.
    def enterClass(self, ctx:CoolParser.ClassContext):
        pass

    # Exit a parse tree produced by CoolParser#class.
    def exitClass(self, ctx:CoolParser.ClassContext):
        pass


    # Enter a parse tree produced by CoolParser#feature.
    def enterFeature(self, ctx:CoolParser.FeatureContext):
        pass

    # Exit a parse tree produced by CoolParser#feature.
    def exitFeature(self, ctx:CoolParser.FeatureContext):
        pass


    # Enter a parse tree produced by CoolParser#formal.
    def enterFormal(self, ctx:CoolParser.FormalContext):
        pass

    # Exit a parse tree produced by CoolParser#formal.
    def exitFormal(self, ctx:CoolParser.FormalContext):
        pass


    # Enter a parse tree produced by CoolParser#expr.
    def enterExpr(self, ctx:CoolParser.ExprContext):
        pass

    # Exit a parse tree produced by CoolParser#expr.
    def exitExpr(self, ctx:CoolParser.ExprContext):
        pass



del CoolParser