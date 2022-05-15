from antlr4 import *
from CoolLexer import CoolLexer
from CoolParser import CoolParser
from CoolListener import CoolListener
from antlr4.tree.Tree import TerminalNodeImpl


def traverse(tree, rule_names, indent=0):
    if tree.getText() == "<EOF>":
        return
    elif isinstance(tree, TerminalNodeImpl):
        print("{0}TOKEN='{1}'".format("  " * indent, tree.getText()))
    else:
        print("{0}{1}".format("  " * indent, rule_names[tree.getRuleIndex()]))
        for child in tree.children:
            traverse(child, rule_names, indent + 1)


class AnalisadorSintatico():
    def __init__(self,arq):
        x=0

    
    def exec(self,arq):
        input = FileStream(arq)
        lexer = CoolLexer(input)
        stream = CommonTokenStream(lexer)
        parser = CoolParser(stream)
        tree = parser.prog()
        printer = CoolListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        traverse(tree, parser.ruleNames)


