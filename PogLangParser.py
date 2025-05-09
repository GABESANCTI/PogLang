# Generated from PogLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,124,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,5,0,12,8,
        0,10,0,12,0,15,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,59,
        8,1,10,1,12,1,62,9,1,1,1,1,1,1,1,1,1,5,1,68,8,1,10,1,12,1,71,9,1,
        1,1,3,1,74,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,82,8,1,10,1,12,1,85,9,
        1,1,1,1,1,1,1,1,1,3,1,91,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,103,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        5,2,117,8,2,10,2,12,2,120,9,2,1,3,1,3,1,3,0,1,4,4,0,2,4,6,0,5,1,
        0,15,16,1,0,13,14,1,0,17,22,1,0,23,24,1,0,11,12,139,0,8,1,0,0,0,
        2,90,1,0,0,0,4,102,1,0,0,0,6,121,1,0,0,0,8,9,5,1,0,0,9,13,5,26,0,
        0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,
        1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,27,0,0,17,18,5,2,0,0,
        18,1,1,0,0,0,19,20,5,3,0,0,20,21,5,33,0,0,21,22,5,31,0,0,22,23,3,
        6,3,0,23,24,5,32,0,0,24,25,3,4,2,0,25,26,5,30,0,0,26,91,1,0,0,0,
        27,28,5,4,0,0,28,29,5,33,0,0,29,30,5,31,0,0,30,31,3,6,3,0,31,32,
        5,32,0,0,32,33,3,4,2,0,33,34,5,30,0,0,34,91,1,0,0,0,35,36,5,33,0,
        0,36,37,5,32,0,0,37,38,3,4,2,0,38,39,5,30,0,0,39,91,1,0,0,0,40,41,
        5,8,0,0,41,42,5,28,0,0,42,43,3,4,2,0,43,44,5,29,0,0,44,45,5,30,0,
        0,45,91,1,0,0,0,46,47,5,33,0,0,47,48,5,32,0,0,48,49,5,9,0,0,49,50,
        5,28,0,0,50,51,5,29,0,0,51,91,5,30,0,0,52,53,5,5,0,0,53,54,5,28,
        0,0,54,55,3,4,2,0,55,56,5,29,0,0,56,60,5,26,0,0,57,59,3,2,1,0,58,
        57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,
        0,62,60,1,0,0,0,63,73,5,27,0,0,64,65,5,6,0,0,65,69,5,26,0,0,66,68,
        3,2,1,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,
        70,72,1,0,0,0,71,69,1,0,0,0,72,74,5,27,0,0,73,64,1,0,0,0,73,74,1,
        0,0,0,74,91,1,0,0,0,75,76,5,7,0,0,76,77,5,28,0,0,77,78,3,4,2,0,78,
        79,5,29,0,0,79,83,5,26,0,0,80,82,3,2,1,0,81,80,1,0,0,0,82,85,1,0,
        0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,83,1,0,0,0,86,87,
        5,27,0,0,87,91,1,0,0,0,88,89,5,10,0,0,89,91,5,30,0,0,90,19,1,0,0,
        0,90,27,1,0,0,0,90,35,1,0,0,0,90,40,1,0,0,0,90,46,1,0,0,0,90,52,
        1,0,0,0,90,75,1,0,0,0,90,88,1,0,0,0,91,3,1,0,0,0,92,93,6,2,-1,0,
        93,94,5,25,0,0,94,103,3,4,2,5,95,96,5,28,0,0,96,97,3,4,2,0,97,98,
        5,29,0,0,98,103,1,0,0,0,99,103,5,33,0,0,100,103,5,34,0,0,101,103,
        5,35,0,0,102,92,1,0,0,0,102,95,1,0,0,0,102,99,1,0,0,0,102,100,1,
        0,0,0,102,101,1,0,0,0,103,118,1,0,0,0,104,105,10,9,0,0,105,106,7,
        0,0,0,106,117,3,4,2,10,107,108,10,8,0,0,108,109,7,1,0,0,109,117,
        3,4,2,9,110,111,10,7,0,0,111,112,7,2,0,0,112,117,3,4,2,8,113,114,
        10,6,0,0,114,115,7,3,0,0,115,117,3,4,2,7,116,104,1,0,0,0,116,107,
        1,0,0,0,116,110,1,0,0,0,116,113,1,0,0,0,117,120,1,0,0,0,118,116,
        1,0,0,0,118,119,1,0,0,0,119,5,1,0,0,0,120,118,1,0,0,0,121,122,7,
        4,0,0,122,7,1,0,0,0,9,13,60,69,73,83,90,102,116,118
    ]

class PogLangParser ( Parser ):

    grammarFileName = "PogLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'start'", "'end'", "'val'", "'var'", 
                     "'if'", "'else'", "'while'", "'println'", "'readLine'", 
                     "'pog'", "'Int'", "'String'", "'+'", "'-'", "'*'", 
                     "'/'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'&&'", "'||'", "'!'", "'{'", "'}'", "'('", "')'", 
                     "';'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>", "START", "END", "VAL", "VAR", "IF", "ELSE", 
                      "WHILE", "PRINTLN", "READLINE", "POG", "INT_TYPE", 
                      "STRING_TYPE", "PLUS", "MINUS", "MULT", "DIV", "EQUALS", 
                      "NEQUALS", "LT", "LTE", "GT", "GTE", "AND", "OR", 
                      "NOT", "LBRACE", "RBRACE", "LPAREN", "RPAREN", "SEMI", 
                      "COLON", "ASSIGN", "ID", "INT", "STRING", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_type = 3

    ruleNames =  [ "program", "statement", "expression", "type" ]

    EOF = Token.EOF
    START=1
    END=2
    VAL=3
    VAR=4
    IF=5
    ELSE=6
    WHILE=7
    PRINTLN=8
    READLINE=9
    POG=10
    INT_TYPE=11
    STRING_TYPE=12
    PLUS=13
    MINUS=14
    MULT=15
    DIV=16
    EQUALS=17
    NEQUALS=18
    LT=19
    LTE=20
    GT=21
    GTE=22
    AND=23
    OR=24
    NOT=25
    LBRACE=26
    RBRACE=27
    LPAREN=28
    RPAREN=29
    SEMI=30
    COLON=31
    ASSIGN=32
    ID=33
    INT=34
    STRING=35
    WS=36
    COMMENT=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START(self):
            return self.getToken(PogLangParser.START, 0)

        def LBRACE(self):
            return self.getToken(PogLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PogLangParser.RBRACE, 0)

        def END(self):
            return self.getToken(PogLangParser.END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PogLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(PogLangParser.StatementContext,i)


        def getRuleIndex(self):
            return PogLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PogLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(PogLangParser.START)
            self.state = 9
            self.match(PogLangParser.LBRACE)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589936056) != 0):
                self.state = 10
                self.statement()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(PogLangParser.RBRACE)
            self.state = 17
            self.match(PogLangParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(PogLangParser.VAL, 0)

        def ID(self):
            return self.getToken(PogLangParser.ID, 0)

        def COLON(self):
            return self.getToken(PogLangParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(PogLangParser.TypeContext,0)


        def ASSIGN(self):
            return self.getToken(PogLangParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(PogLangParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(PogLangParser.SEMI, 0)

        def VAR(self):
            return self.getToken(PogLangParser.VAR, 0)

        def PRINTLN(self):
            return self.getToken(PogLangParser.PRINTLN, 0)

        def LPAREN(self):
            return self.getToken(PogLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PogLangParser.RPAREN, 0)

        def READLINE(self):
            return self.getToken(PogLangParser.READLINE, 0)

        def IF(self):
            return self.getToken(PogLangParser.IF, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(PogLangParser.LBRACE)
            else:
                return self.getToken(PogLangParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(PogLangParser.RBRACE)
            else:
                return self.getToken(PogLangParser.RBRACE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PogLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(PogLangParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(PogLangParser.ELSE, 0)

        def WHILE(self):
            return self.getToken(PogLangParser.WHILE, 0)

        def POG(self):
            return self.getToken(PogLangParser.POG, 0)

        def getRuleIndex(self):
            return PogLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PogLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(PogLangParser.VAL)
                self.state = 20
                self.match(PogLangParser.ID)
                self.state = 21
                self.match(PogLangParser.COLON)
                self.state = 22
                self.type_()
                self.state = 23
                self.match(PogLangParser.ASSIGN)
                self.state = 24
                self.expression(0)
                self.state = 25
                self.match(PogLangParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(PogLangParser.VAR)
                self.state = 28
                self.match(PogLangParser.ID)
                self.state = 29
                self.match(PogLangParser.COLON)
                self.state = 30
                self.type_()
                self.state = 31
                self.match(PogLangParser.ASSIGN)
                self.state = 32
                self.expression(0)
                self.state = 33
                self.match(PogLangParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(PogLangParser.ID)
                self.state = 36
                self.match(PogLangParser.ASSIGN)
                self.state = 37
                self.expression(0)
                self.state = 38
                self.match(PogLangParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.match(PogLangParser.PRINTLN)
                self.state = 41
                self.match(PogLangParser.LPAREN)
                self.state = 42
                self.expression(0)
                self.state = 43
                self.match(PogLangParser.RPAREN)
                self.state = 44
                self.match(PogLangParser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.match(PogLangParser.ID)
                self.state = 47
                self.match(PogLangParser.ASSIGN)
                self.state = 48
                self.match(PogLangParser.READLINE)
                self.state = 49
                self.match(PogLangParser.LPAREN)
                self.state = 50
                self.match(PogLangParser.RPAREN)
                self.state = 51
                self.match(PogLangParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 52
                self.match(PogLangParser.IF)
                self.state = 53
                self.match(PogLangParser.LPAREN)
                self.state = 54
                self.expression(0)
                self.state = 55
                self.match(PogLangParser.RPAREN)
                self.state = 56
                self.match(PogLangParser.LBRACE)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589936056) != 0):
                    self.state = 57
                    self.statement()
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 63
                self.match(PogLangParser.RBRACE)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 64
                    self.match(PogLangParser.ELSE)
                    self.state = 65
                    self.match(PogLangParser.LBRACE)
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589936056) != 0):
                        self.state = 66
                        self.statement()
                        self.state = 71
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 72
                    self.match(PogLangParser.RBRACE)


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 75
                self.match(PogLangParser.WHILE)
                self.state = 76
                self.match(PogLangParser.LPAREN)
                self.state = 77
                self.expression(0)
                self.state = 78
                self.match(PogLangParser.RPAREN)
                self.state = 79
                self.match(PogLangParser.LBRACE)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589936056) != 0):
                    self.state = 80
                    self.statement()
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 86
                self.match(PogLangParser.RBRACE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 88
                self.match(PogLangParser.POG)
                self.state = 89
                self.match(PogLangParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def NOT(self):
            return self.getToken(PogLangParser.NOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PogLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PogLangParser.ExpressionContext,i)


        def LPAREN(self):
            return self.getToken(PogLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PogLangParser.RPAREN, 0)

        def ID(self):
            return self.getToken(PogLangParser.ID, 0)

        def INT(self):
            return self.getToken(PogLangParser.INT, 0)

        def STRING(self):
            return self.getToken(PogLangParser.STRING, 0)

        def MULT(self):
            return self.getToken(PogLangParser.MULT, 0)

        def DIV(self):
            return self.getToken(PogLangParser.DIV, 0)

        def PLUS(self):
            return self.getToken(PogLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(PogLangParser.MINUS, 0)

        def EQUALS(self):
            return self.getToken(PogLangParser.EQUALS, 0)

        def NEQUALS(self):
            return self.getToken(PogLangParser.NEQUALS, 0)

        def LT(self):
            return self.getToken(PogLangParser.LT, 0)

        def LTE(self):
            return self.getToken(PogLangParser.LTE, 0)

        def GT(self):
            return self.getToken(PogLangParser.GT, 0)

        def GTE(self):
            return self.getToken(PogLangParser.GTE, 0)

        def AND(self):
            return self.getToken(PogLangParser.AND, 0)

        def OR(self):
            return self.getToken(PogLangParser.OR, 0)

        def getRuleIndex(self):
            return PogLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PogLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 93
                self.match(PogLangParser.NOT)
                self.state = 94
                self.expression(5)
                pass
            elif token in [28]:
                self.state = 95
                self.match(PogLangParser.LPAREN)
                self.state = 96
                self.expression(0)
                self.state = 97
                self.match(PogLangParser.RPAREN)
                pass
            elif token in [33]:
                self.state = 99
                self.match(PogLangParser.ID)
                pass
            elif token in [34]:
                self.state = 100
                self.match(PogLangParser.INT)
                pass
            elif token in [35]:
                self.state = 101
                self.match(PogLangParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 116
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = PogLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 104
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 105
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 106
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = PogLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 107
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 108
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 109
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = PogLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 110
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 111
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 112
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = PogLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 113
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 114
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 115
                        self.expression(7)
                        pass

             
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(PogLangParser.INT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(PogLangParser.STRING_TYPE, 0)

        def getRuleIndex(self):
            return PogLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = PogLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         




