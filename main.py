import sys
from antlr4 import *
from PogLangLexer import PogLangLexer
from PogLangParser import PogLangParser
from PogLangRunner import PogLangRunner

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py arquivo.pog")
        return

    input_stream = FileStream(sys.argv[1], encoding='utf-8')
    lexer = PogLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PogLangParser(stream)
    tree = parser.program()

    runner = PogLangRunner()
    runner.visit(tree)

if __name__ == '__main__':
    main()
