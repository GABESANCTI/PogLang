from antlr4 import FileStream, CommonTokenStream
from PogLangLexer import PogLangLexer
from PogLangParser import PogLangParser
from PogLangErrorListener import PogLangErrorListener
from PogLangExecutor import PogLangExecutor

def main():
    input_stream = FileStream("testavar.pog", encoding="utf-8")

    lexer = PogLangLexer(input_stream)
    lexer_error_listener = PogLangErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_error_listener)

    token_stream = CommonTokenStream(lexer)

    parser = PogLangParser(token_stream)
    parser_error_listener = PogLangErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(parser_error_listener)

    tree = parser.program()

    if lexer_error_listener.has_errors or parser_error_listener.has_errors:
        print("Erros detectados. Execução abortada.")
        return

    executor = PogLangExecutor()
    executor.visitProgram(tree)  # <- uso direto, sem .visit()

if __name__ == "__main__":
    main()
