# Generated from Fibo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FiboParser import FiboParser
else:
    from FiboParser import FiboParser

# This class defines a complete generic visitor for a parse tree produced by FiboParser.

class FiboVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FiboParser#prog.
    def visitProg(self, ctx:FiboParser.ProgContext):
        return self.visitChildren(ctx)



del FiboParser