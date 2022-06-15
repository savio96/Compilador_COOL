from antlr4 import *
from CoolLexer import CoolLexer
from CoolParser import CoolParser
from CoolListener import CoolListener
from antlr4.tree.Tree import TerminalNodeImpl
from AntlrToProg import *

class AnalisadorSemantico():
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def exec(self):
        input = FileStream(self.arquivo)
        lexer = CoolLexer(input)
        tokens = CommonTokenStream(lexer)
        parser = CoolParser(tokens)

        tree = parser.prog()
        progVisitor = AntlrToProg()
        progVisitor.visit(tree)
        progVisitor.mostrar()