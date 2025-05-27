from PogLangParser import PogLangParser
from PogLangVisitor import PogLangVisitor

class SemanticAnalyzer(PogLangVisitor):
    def __init__(self):
        self.symbol_table = {}  # nome -> tipo
        self.errors = []

    def log(self, msg):
        print(f"[SEMÂNTICO] {msg}")  # pode comentar isso se quiser menos logs

    def error(self, msg):
        self.errors.append(msg)
        print(f"[Erro Semântico] {msg}")

    def visitProgram(self, ctx: PogLangParser.ProgramContext):
        self.log("Iniciando análise semântica...")
        self.visitChildren(ctx)
        if not self.errors:
            print("Análise semântica concluída sem erros!")
        else:
            print(f"Análise semântica com {len(self.errors)} erro(s).")

    def visitStatement(self, ctx: PogLangParser.StatementContext):
        if ctx.VAL() or ctx.VAR():
            var_type = ctx.type_().getText()
            var_name = ctx.ID().getText()
            self.log(f"Declarando variável '{var_name}' do tipo '{var_type}'")

            if var_name in self.symbol_table:
                self.error(f"Variável '{var_name}' já declarada.")
            else:
                expr_type = self.visit(ctx.expression())
                if expr_type and expr_type != var_type:
                    self.error(f"Tipo incompatível na declaração de '{var_name}': esperado '{var_type}', encontrado '{expr_type}'.")
                self.symbol_table[var_name] = var_type
            return None

        if ctx.ID() and ctx.ASSIGN():
            var_name = ctx.ID().getText()
            if var_name not in self.symbol_table:
                self.error(f"Variável '{var_name}' não declarada antes do uso.")
            else:
                var_type = self.symbol_table[var_name]
                expr_type = self.visit(ctx.expression())
                if expr_type and expr_type != var_type:
                    self.error(f"Tipo incompatível na atribuição para '{var_name}': esperado '{var_type}', encontrado '{expr_type}'.")
            return None

        return self.visitChildren(ctx)

    def visitLogicalOrExpression(self, ctx: PogLangParser.LogicalOrExpressionContext):
        if len(ctx.logicalAndExpression()) == 1:
            return self.visit(ctx.logicalAndExpression(0))

        left = self.visit(ctx.logicalAndExpression(0))
        right = self.visit(ctx.logicalAndExpression(1))
        if left != "Int" or right != "Int":
            self.error("Operador '||' requer inteiros.")
            return None
        return "Int"

    def visitLogicalAndExpression(self, ctx: PogLangParser.LogicalAndExpressionContext):
        if len(ctx.equalityExpression()) == 1:
            return self.visit(ctx.equalityExpression(0))

        left = self.visit(ctx.equalityExpression(0))
        right = self.visit(ctx.equalityExpression(1))
        if left != "Int" or right != "Int":
            self.error("Operador '&&' requer inteiros.")
            return None
        return "Int"

    def visitEqualityExpression(self, ctx: PogLangParser.EqualityExpressionContext):
        if len(ctx.relationalExpression()) == 1:
            return self.visit(ctx.relationalExpression(0))

        left = self.visit(ctx.relationalExpression(0))
        right = self.visit(ctx.relationalExpression(1))
        if left != right:
            self.error(f"Operador de igualdade entre tipos diferentes: '{left}' e '{right}'.")
            return None
        return "Int"

    def visitRelationalExpression(self, ctx: PogLangParser.RelationalExpressionContext):
        if len(ctx.additiveExpression()) == 1:
            return self.visit(ctx.additiveExpression(0))

        left = self.visit(ctx.additiveExpression(0))
        right = self.visit(ctx.additiveExpression(1))
        if left != "Int" or right != "Int":
            self.error("Operador relacional requer inteiros.")
            return None
        return "Int"

    def visitAdditiveExpression(self, ctx: PogLangParser.AdditiveExpressionContext):
        if len(ctx.multiplicativeExpression()) == 1:
            return self.visit(ctx.multiplicativeExpression(0))

        left = self.visit(ctx.multiplicativeExpression(0))
        right = self.visit(ctx.multiplicativeExpression(1))
        if left != "Int" or right != "Int":
            self.error("Operador '+' ou '-' requer inteiros.")
            return None
        return "Int"

    def visitMultiplicativeExpression(self, ctx: PogLangParser.MultiplicativeExpressionContext):
        if len(ctx.unaryExpression()) == 1:
            return self.visit(ctx.unaryExpression(0))

        left = self.visit(ctx.unaryExpression(0))
        right = self.visit(ctx.unaryExpression(1))
        op = ctx.getChild(1).getText()

        if right == "Int":
            right_text = ctx.unaryExpression(1).getText()
            if op == '/' and right_text == '0':
                self.error("Divisão por zero detectada.")
                return None

        if left != "Int" or right != "Int":
            self.error(f"Operador '{op}' requer inteiros.")
            return None
        return "Int"

    def visitUnaryExpression(self, ctx: PogLangParser.UnaryExpressionContext):
        if ctx.NOT():
            expr_type = self.visit(ctx.unaryExpression())
            if expr_type != "Int":
                self.error("Operador '!' requer inteiro.")
                return None
            return "Int"
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx: PogLangParser.PrimaryContext):
        if ctx.INT():
            return "Int"
        if ctx.STRING():
            return "String"
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name not in self.symbol_table:
                self.error(f"Variável '{var_name}' usada sem declaração.")
                return None
            return self.symbol_table[var_name]
        if ctx.expression():
            return self.visit(ctx.expression())
        return None
