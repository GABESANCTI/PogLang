from antlr4.error.ErrorListener import ErrorListener

class PogLangErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        found = offendingSymbol.text if offendingSymbol else "EOF"
        print(f"ERRO SINTÁTICO [Linha {line}, Coluna {column}]: {msg} (encontrado '{found}')")
        exit(1)
