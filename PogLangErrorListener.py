from antlr4.error.ErrorListener import ErrorListener

class PogLangErrorListener(ErrorListener):
    def __init__(self):
        super(PogLangErrorListener, self).__init__()
        self.has_errors = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_errors = True
        print(f"[Erro sintático] Linha {line}:{column} - {msg}")
