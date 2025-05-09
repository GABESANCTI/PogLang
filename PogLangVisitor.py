# Generated from PogLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PogLangParser import PogLangParser
else:
    from PogLangParser import PogLangParser

# This class defines a complete generic visitor for a parse tree produced by PogLangParser.

class PogLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PogLangParser#program.
    def visitProgram(self, ctx:PogLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PogLangParser#statement.
    def visitStatement(self, ctx:PogLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PogLangParser#expression.
    def visitExpression(self, ctx:PogLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PogLangParser#type.
    def visitType(self, ctx:PogLangParser.TypeContext):
        return self.visitChildren(ctx)



del PogLangParser