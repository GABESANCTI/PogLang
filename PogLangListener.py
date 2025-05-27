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


    # Enter a parse tree produced by PogLangParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:PogLangParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by PogLangParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:PogLangParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by PogLangParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:PogLangParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by PogLangParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:PogLangParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by PogLangParser#equalityExpression.
    def enterEqualityExpression(self, ctx:PogLangParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by PogLangParser#equalityExpression.
    def exitEqualityExpression(self, ctx:PogLangParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by PogLangParser#relationalExpression.
    def enterRelationalExpression(self, ctx:PogLangParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by PogLangParser#relationalExpression.
    def exitRelationalExpression(self, ctx:PogLangParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by PogLangParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:PogLangParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by PogLangParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:PogLangParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by PogLangParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:PogLangParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by PogLangParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:PogLangParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by PogLangParser#unaryExpression.
    def enterUnaryExpression(self, ctx:PogLangParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by PogLangParser#unaryExpression.
    def exitUnaryExpression(self, ctx:PogLangParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by PogLangParser#primary.
    def enterPrimary(self, ctx:PogLangParser.PrimaryContext):
        pass

    # Exit a parse tree produced by PogLangParser#primary.
    def exitPrimary(self, ctx:PogLangParser.PrimaryContext):
        pass


    # Enter a parse tree produced by PogLangParser#type.
    def enterType(self, ctx:PogLangParser.TypeContext):
        pass

    # Exit a parse tree produced by PogLangParser#type.
    def exitType(self, ctx:PogLangParser.TypeContext):
        pass



del PogLangParser