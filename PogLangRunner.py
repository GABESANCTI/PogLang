from PogLangVisitor import PogLangVisitor

class PogLangRunner(PogLangVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitStatement(self, ctx):
        if ctx.VAR():
            name = ctx.ID().getText()
            value = self.visit(ctx.expression())
            self.variables[name] = value
        elif ctx.VAL():
            name = ctx.ID().getText()
            value = self.visit(ctx.expression())
            self.variables[name] = value  # VAL e VAR tratados igual por enquanto
        elif ctx.PRINTLN():
            value = self.visit(ctx.expression())
            print(value)
        elif ctx.ASSIGN() and ctx.ID():
            name = ctx.ID().getText()
            value = self.visit(ctx.expression())
            self.variables[name] = value

    def visitExpression(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]  # Remove aspas
        elif ctx.ID():
            return self.variables.get(ctx.ID().getText(), 0)
        elif ctx.op:
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            op = ctx.op.text
            if op == '+': return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/': return left // right if right != 0 else 0
        return None
