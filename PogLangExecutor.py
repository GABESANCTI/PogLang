from PogLangParser import PogLangParser
from PogLangVisitor import PogLangVisitor

class PogLangExecutor(PogLangVisitor):
    def __init__(self):
        self.symbols = {}

    def visitProgram(self, ctx: PogLangParser.ProgramContext):
        print("[SEMÂNTICO] Visitando programa")
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitStatement(self, ctx: PogLangParser.StatementContext):
        if ctx.VAL() or ctx.VAR():
            var_name = ctx.ID().getText()
            var_type = ctx.type_().getText()
            if var_name in self.symbols:
                print(f"[Erro Semântico] variável '{var_name}' já declarada.")
                return
            value = self.visit(ctx.expression())
            self.symbols[var_name] = {'type': var_type, 'value': value}
        elif ctx.ID() and ctx.ASSIGN() and ctx.expression():
            var_name = ctx.ID().getText()
            if var_name not in self.symbols:
                print(f"[Erro Semântico] variável '{var_name}' não declarada.")
                return
            value = self.visit(ctx.expression())
            self.symbols[var_name]['value'] = value
        elif ctx.PRINTLN():
            value = self.visit(ctx.expression())
            print(value)
        elif ctx.ID() and ctx.READLINE():
            var_name = ctx.ID().getText()
            if var_name not in self.symbols:
                print(f"[Erro Semântico] variável '{var_name}' não declarada.")
                return
            user_input = input()
            if self.symbols[var_name]['type'] == 'Int':
                try:
                    user_input = int(user_input)
                except ValueError:
                    print(f"[Erro Semântico] Entrada inválida para variável Int '{var_name}'")
                    return
            self.symbols[var_name]['value'] = user_input
        elif ctx.IF():
            condition = self.visit(ctx.expression())
            if condition:
                for stmt in ctx.statement(0).statement():
                    self.visit(stmt)
            elif ctx.ELSE():
                for stmt in ctx.statement(1).statement():
                    self.visit(stmt)
        elif ctx.WHILE():
            while self.visit(ctx.expression()):
                for stmt in ctx.statement(0).statement():
                    self.visit(stmt)
        elif ctx.POG():
            print("Poggers")

    def visitExpression(self, ctx):
        return self.visit(ctx.logicalOrExpression())

    def visitLogicalOrExpression(self, ctx):
        result = self.visit(ctx.logicalAndExpression(0))
        for i in range(1, len(ctx.logicalAndExpression())):
            right = self.visit(ctx.logicalAndExpression(i))
            result = 1 if result or right else 0
        return result

    def visitLogicalAndExpression(self, ctx):
        result = self.visit(ctx.equalityExpression(0))
        for i in range(1, len(ctx.equalityExpression())):
            right = self.visit(ctx.equalityExpression(i))
            result = 1 if result and right else 0
        return result

    def visitEqualityExpression(self, ctx):
        result = self.visit(ctx.relationalExpression(0))
        for i in range(1, len(ctx.relationalExpression())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.relationalExpression(i))
            if op == '==':
                result = 1 if result == right else 0
            elif op == '!=':
                result = 1 if result != right else 0
        return result

    def visitRelationalExpression(self, ctx):
        result = self.visit(ctx.additiveExpression(0))
        for i in range(1, len(ctx.additiveExpression())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.additiveExpression(i))
            if op == '<':
                result = 1 if result < right else 0
            elif op == '<=':
                result = 1 if result <= right else 0
            elif op == '>':
                result = 1 if result > right else 0
            elif op == '>=':
                result = 1 if result >= right else 0
        return result

    def visitAdditiveExpression(self, ctx):
        result = self.visit(ctx.multiplicativeExpression(0))
        for i in range(1, len(ctx.multiplicativeExpression())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.multiplicativeExpression(i))
            result = result + right if op == '+' else result - right
        return result

    def visitMultiplicativeExpression(self, ctx):
        result = self.visit(ctx.unaryExpression(0))
        for i in range(1, len(ctx.unaryExpression())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.unaryExpression(i))
            if op == '/':
                if right == 0:
                    print("[Erro Semântico] divisão por zero")
                    return 0
                result = result // right
            elif op == '*':
                result = result * right
        return result

    def visitUnaryExpression(self, ctx):
        if ctx.NOT():
            val = self.visit(ctx.unaryExpression())
            return 0 if val else 1
        else:
            return self.visit(ctx.primary())

    def visitPrimary(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.ID():
            name = ctx.ID().getText()
            if name not in self.symbols:
                print(f"[Erro Semântico] variável '{name}' não declarada.")
                return 0
            return self.symbols[name]['value']
        elif ctx.expression():
            return self.visit(ctx.expression())
