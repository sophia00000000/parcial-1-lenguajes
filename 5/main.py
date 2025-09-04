import sys
from antlr4 import *
from FiboLexer import FiboLexer
from FiboParser import FiboParser
from MyFiboVisitor import MyFiboVisitor

def main():
    entrada = InputStream(input("Ingrese FIBO(): "))
    lexer = FiboLexer(entrada)
    tokens = CommonTokenStream(lexer)
    parser = FiboParser(tokens)
    tree = parser.prog()

    visitor = MyFiboVisitor()
    resultado = visitor.visit(tree)

    print("Resultado:", ", ".join(map(str, resultado)))

if __name__ == '__main__':
    main()
