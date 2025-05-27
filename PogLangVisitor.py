class PogLangVisitor:
    def __init__(self):
        self.memory = {}
        self.errors = []

    def log(self, msg):
        print(f"[SEMÂNTICO] {msg}")

    def visitProgram(self, ctx):
        self.log("Visitando programa")
        for child in ctx.children:
            self.visit(child)
        if self.errors:
            print("\nErros encontrados:")
            for e in self.errors:
                print(e)
        else:
            print("\nExecução finalizada com sucesso.")
            print("Memória final:", self.memory)

    def visitDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        self.log(f"Declarando variável '{var_name}'")
        if var_name in self.memory:
            self.errors.append(f"[Erro Semântico] Variável '{var_name}' declarada duas vezes.")
        else:
            self.memory[var_name] = None

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        self.log(f"Atribuindo valor à variável '{var_name}'")
        if var_name not in self.memory:
            self.errors.append(f"[Erro Semântico] Variável '{var_name}' não declarada.")
            return
        value = self.visit(ctx.expr())
        self.memory[var_name] = value

    def visitPrint(self, ctx):
        value = self.visit(ctx.expr())
        print(f">>> {value}")

    def visitExpr(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name not in self.memory:
                self.errors.append(f"[Erro Semântico] Variável '{var_name}' não declarada.")
                return None
            val = self.memory[var_name]
            if val is None:
                self.errors.append(f"[Erro Semântico] Variável '{var_name}' sem valor atribuído.")
            return val
        elif ctx.getChildCount() == 3:
            left = self.visit(ctx.expr(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expr(1))

            if left is None or right is None:
                return None

            if not isinstance(left, int) or not isinstance(right, int):
                self.errors.append(f"[Erro Semântico] Operação inválida com tipos: {left} e {right}")
                return None

            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                if right == 0:
                    self.errors.append("[Erro Semântico] Divisão por zero.")
                    return None
                return left // right
        elif ctx.expr():
            return self.visit(ctx.expr(0))

    def visit(self, ctx):
        method_name = 'visit' + type(ctx).__name__.replace('Context', '')
        visitor = getattr(self, method_name, self.visitChildren)
        return visitor(ctx)

    def visitChildren(self, ctx):
        result = None
        for child in ctx.getChildren():
            res = self.visit(child)
            if res is not None:
                result = res
        return result
