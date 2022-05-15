# Generated from Cool.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CoolParser import CoolParser
else:
    from CoolParser import CoolParser

# This class defines a complete generic visitor for a parse tree produced by CoolParser.

class CoolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CoolParser#prog.
    def visitProg(self, ctx:CoolParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#class.
    def visitClass(self, ctx:CoolParser.ClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#feature.
    def visitFeature(self, ctx:CoolParser.FeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#formal.
    def visitFormal(self, ctx:CoolParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoolParser#expr.
    def visitExpr(self, ctx:CoolParser.ExprContext):
        return self.visitChildren(ctx)



del CoolParser