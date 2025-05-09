# Generated from PogLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PogLangParser import PogLangParser
else:
    from PogLangParser import PogLangParser

# This class defines a complete listener for a parse tree produced by PogLangParser.
class PogLangListener(ParseTreeListener):

    # Enter a parse tree produced by PogLangParser#program.
    def enterProgram(self, ctx:PogLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by PogLangParser#program.
    def exitProgram(self, ctx:PogLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by PogLangParser#statement.
    def enterStatement(self, ctx:PogLangParser.StatementContext):
        pass

    # Exit a parse tree produced by PogLangParser#statement.
    def exitStatement(self, ctx:PogLangParser.StatementContext):
        pass


    # Enter a parse tree produced by PogLangParser#expression.
    def enterExpression(self, ctx:PogLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PogLangParser#expression.
    def exitExpression(self, ctx:PogLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PogLangParser#type.
    def enterType(self, ctx:PogLangParser.TypeContext):
        pass

    # Exit a parse tree produced by PogLangParser#type.
    def exitType(self, ctx:PogLangParser.TypeContext):
        pass



del PogLangParser