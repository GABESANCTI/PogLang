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
        4,1,37,175,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,5,0,28,
        8,0,10,0,12,0,31,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,
        75,8,1,10,1,12,1,78,9,1,1,1,1,1,1,1,1,1,5,1,84,8,1,10,1,12,1,87,
        9,1,1,1,3,1,90,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,98,8,1,10,1,12,1,
        101,9,1,1,1,1,1,1,1,1,1,3,1,107,8,1,1,2,1,2,1,3,1,3,1,3,5,3,114,
        8,3,10,3,12,3,117,9,3,1,4,1,4,1,4,5,4,122,8,4,10,4,12,4,125,9,4,
        1,5,1,5,1,5,5,5,130,8,5,10,5,12,5,133,9,5,1,6,1,6,1,6,5,6,138,8,
        6,10,6,12,6,141,9,6,1,7,1,7,1,7,5,7,146,8,7,10,7,12,7,149,9,7,1,
        8,1,8,1,8,5,8,154,8,8,10,8,12,8,157,9,8,1,9,1,9,1,9,3,9,162,8,9,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,171,8,10,1,11,1,11,1,11,
        0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,5,1,0,17,18,1,0,19,22,1,
        0,13,14,1,0,15,16,1,0,11,12,184,0,24,1,0,0,0,2,106,1,0,0,0,4,108,
        1,0,0,0,6,110,1,0,0,0,8,118,1,0,0,0,10,126,1,0,0,0,12,134,1,0,0,
        0,14,142,1,0,0,0,16,150,1,0,0,0,18,161,1,0,0,0,20,170,1,0,0,0,22,
        172,1,0,0,0,24,25,5,1,0,0,25,29,5,26,0,0,26,28,3,2,1,0,27,26,1,0,
        0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,
        1,0,0,0,32,33,5,27,0,0,33,34,5,2,0,0,34,1,1,0,0,0,35,36,5,3,0,0,
        36,37,5,33,0,0,37,38,5,31,0,0,38,39,3,22,11,0,39,40,5,32,0,0,40,
        41,3,4,2,0,41,42,5,30,0,0,42,107,1,0,0,0,43,44,5,4,0,0,44,45,5,33,
        0,0,45,46,5,31,0,0,46,47,3,22,11,0,47,48,5,32,0,0,48,49,3,4,2,0,
        49,50,5,30,0,0,50,107,1,0,0,0,51,52,5,33,0,0,52,53,5,32,0,0,53,54,
        3,4,2,0,54,55,5,30,0,0,55,107,1,0,0,0,56,57,5,8,0,0,57,58,5,28,0,
        0,58,59,3,4,2,0,59,60,5,29,0,0,60,61,5,30,0,0,61,107,1,0,0,0,62,
        63,5,33,0,0,63,64,5,32,0,0,64,65,5,9,0,0,65,66,5,28,0,0,66,67,5,
        29,0,0,67,107,5,30,0,0,68,69,5,5,0,0,69,70,5,28,0,0,70,71,3,4,2,
        0,71,72,5,29,0,0,72,76,5,26,0,0,73,75,3,2,1,0,74,73,1,0,0,0,75,78,
        1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,
        79,89,5,27,0,0,80,81,5,6,0,0,81,85,5,26,0,0,82,84,3,2,1,0,83,82,
        1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,
        87,85,1,0,0,0,88,90,5,27,0,0,89,80,1,0,0,0,89,90,1,0,0,0,90,107,
        1,0,0,0,91,92,5,7,0,0,92,93,5,28,0,0,93,94,3,4,2,0,94,95,5,29,0,
        0,95,99,5,26,0,0,96,98,3,2,1,0,97,96,1,0,0,0,98,101,1,0,0,0,99,97,
        1,0,0,0,99,100,1,0,0,0,100,102,1,0,0,0,101,99,1,0,0,0,102,103,5,
        27,0,0,103,107,1,0,0,0,104,105,5,10,0,0,105,107,5,30,0,0,106,35,
        1,0,0,0,106,43,1,0,0,0,106,51,1,0,0,0,106,56,1,0,0,0,106,62,1,0,
        0,0,106,68,1,0,0,0,106,91,1,0,0,0,106,104,1,0,0,0,107,3,1,0,0,0,
        108,109,3,6,3,0,109,5,1,0,0,0,110,115,3,8,4,0,111,112,5,24,0,0,112,
        114,3,8,4,0,113,111,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,
        116,1,0,0,0,116,7,1,0,0,0,117,115,1,0,0,0,118,123,3,10,5,0,119,120,
        5,23,0,0,120,122,3,10,5,0,121,119,1,0,0,0,122,125,1,0,0,0,123,121,
        1,0,0,0,123,124,1,0,0,0,124,9,1,0,0,0,125,123,1,0,0,0,126,131,3,
        12,6,0,127,128,7,0,0,0,128,130,3,12,6,0,129,127,1,0,0,0,130,133,
        1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,11,1,0,0,0,133,131,1,
        0,0,0,134,139,3,14,7,0,135,136,7,1,0,0,136,138,3,14,7,0,137,135,
        1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,13,1,
        0,0,0,141,139,1,0,0,0,142,147,3,16,8,0,143,144,7,2,0,0,144,146,3,
        16,8,0,145,143,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,1,
        0,0,0,148,15,1,0,0,0,149,147,1,0,0,0,150,155,3,18,9,0,151,152,7,
        3,0,0,152,154,3,18,9,0,153,151,1,0,0,0,154,157,1,0,0,0,155,153,1,
        0,0,0,155,156,1,0,0,0,156,17,1,0,0,0,157,155,1,0,0,0,158,159,5,25,
        0,0,159,162,3,18,9,0,160,162,3,20,10,0,161,158,1,0,0,0,161,160,1,
        0,0,0,162,19,1,0,0,0,163,171,5,34,0,0,164,171,5,35,0,0,165,171,5,
        33,0,0,166,167,5,28,0,0,167,168,3,4,2,0,168,169,5,29,0,0,169,171,
        1,0,0,0,170,163,1,0,0,0,170,164,1,0,0,0,170,165,1,0,0,0,170,166,
        1,0,0,0,171,21,1,0,0,0,172,173,7,4,0,0,173,23,1,0,0,0,14,29,76,85,
        89,99,106,115,123,131,139,147,155,161,170
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
    RULE_logicalOrExpression = 3
    RULE_logicalAndExpression = 4
    RULE_equalityExpression = 5
    RULE_relationalExpression = 6
    RULE_additiveExpression = 7
    RULE_multiplicativeExpression = 8
    RULE_unaryExpression = 9
    RULE_primary = 10
    RULE_type = 11

    ruleNames =  [ "program", "statement", "expression", "logicalOrExpression", 
                   "logicalAndExpression", "equalityExpression", "relationalExpression", 
                   "additiveExpression", "multiplicativeExpression", "unaryExpression", 
                   "primary", "type" ]

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




    def program(self):

        localctx = PogLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(PogLangParser.START)
            self.state = 25
            self.match(PogLangParser.LBRACE)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589936056) != 0):
                self.state = 26
                self.statement()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(PogLangParser.RBRACE)
            self.state = 33
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




    def statement(self):

        localctx = PogLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(PogLangParser.VAL)
                self.state = 36
                self.match(PogLangParser.ID)
                self.state = 37
                self.match(PogLangParser.COLON)
                self.state = 38
                self.type_()
                self.state = 39
                self.match(PogLangParser.ASSIGN)
                self.state = 40
                self.expression()
                self.state = 41
                self.match(PogLangParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(PogLangParser.VAR)
                self.state = 44
                self.match(PogLangParser.ID)
                self.state = 45
                self.match(PogLangParser.COLON)
                self.state = 46
                self.type_()
                self.state = 47
                self.match(PogLangParser.ASSIGN)
                self.state = 48
                self.expression()
                self.state = 49
                self.match(PogLangParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.match(PogLangParser.ID)
                self.state = 52
                self.match(PogLangParser.ASSIGN)
                self.state = 53
                self.expression()
                self.state = 54
                self.match(PogLangParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.match(PogLangParser.PRINTLN)
                self.state = 57
                self.match(PogLangParser.LPAREN)
                self.state = 58
                self.expression()
                self.state = 59
                self.match(PogLangParser.RPAREN)
                self.state = 60
                self.match(PogLangParser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 62
                self.match(PogLangParser.ID)
                self.state = 63
                self.match(PogLangParser.ASSIGN)
                self.state = 64
                self.match(PogLangParser.READLINE)
                self.state = 65
                self.match(PogLangParser.LPAREN)
                self.state = 66
                self.match(PogLangParser.RPAREN)
                self.state = 67
                self.match(PogLangParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 68
                self.match(PogLangParser.IF)
                self.state = 69
                self.match(PogLangParser.LPAREN)
                self.state = 70
                self.expression()
                self.state = 71
                self.match(PogLangParser.RPAREN)
                self.state = 72
                self.match(PogLangParser.LBRACE)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589936056) != 0):
                    self.state = 73
                    self.statement()
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 79
                self.match(PogLangParser.RBRACE)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 80
                    self.match(PogLangParser.ELSE)
                    self.state = 81
                    self.match(PogLangParser.LBRACE)
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589936056) != 0):
                        self.state = 82
                        self.statement()
                        self.state = 87
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 88
                    self.match(PogLangParser.RBRACE)


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 91
                self.match(PogLangParser.WHILE)
                self.state = 92
                self.match(PogLangParser.LPAREN)
                self.state = 93
                self.expression()
                self.state = 94
                self.match(PogLangParser.RPAREN)
                self.state = 95
                self.match(PogLangParser.LBRACE)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589936056) != 0):
                    self.state = 96
                    self.statement()
                    self.state = 101
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 102
                self.match(PogLangParser.RBRACE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 104
                self.match(PogLangParser.POG)
                self.state = 105
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

        def logicalOrExpression(self):
            return self.getTypedRuleContext(PogLangParser.LogicalOrExpressionContext,0)


        def getRuleIndex(self):
            return PogLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = PogLangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.logicalOrExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PogLangParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(PogLangParser.LogicalAndExpressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(PogLangParser.OR)
            else:
                return self.getToken(PogLangParser.OR, i)

        def getRuleIndex(self):
            return PogLangParser.RULE_logicalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)




    def logicalOrExpression(self):

        localctx = PogLangParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.logicalAndExpression()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 111
                self.match(PogLangParser.OR)
                self.state = 112
                self.logicalAndExpression()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PogLangParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(PogLangParser.EqualityExpressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(PogLangParser.AND)
            else:
                return self.getToken(PogLangParser.AND, i)

        def getRuleIndex(self):
            return PogLangParser.RULE_logicalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)




    def logicalAndExpression(self):

        localctx = PogLangParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.equalityExpression()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 119
                self.match(PogLangParser.AND)
                self.state = 120
                self.equalityExpression()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PogLangParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(PogLangParser.RelationalExpressionContext,i)


        def EQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(PogLangParser.EQUALS)
            else:
                return self.getToken(PogLangParser.EQUALS, i)

        def NEQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(PogLangParser.NEQUALS)
            else:
                return self.getToken(PogLangParser.NEQUALS, i)

        def getRuleIndex(self):
            return PogLangParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)




    def equalityExpression(self):

        localctx = PogLangParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.relationalExpression()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 127
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 128
                self.relationalExpression()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PogLangParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(PogLangParser.AdditiveExpressionContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(PogLangParser.LT)
            else:
                return self.getToken(PogLangParser.LT, i)

        def LTE(self, i:int=None):
            if i is None:
                return self.getTokens(PogLangParser.LTE)
            else:
                return self.getToken(PogLangParser.LTE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(PogLangParser.GT)
            else:
                return self.getToken(PogLangParser.GT, i)

        def GTE(self, i:int=None):
            if i is None:
                return self.getTokens(PogLangParser.GTE)
            else:
                return self.getToken(PogLangParser.GTE, i)

        def getRuleIndex(self):
            return PogLangParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)




    def relationalExpression(self):

        localctx = PogLangParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.additiveExpression()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0):
                self.state = 135
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 136
                self.additiveExpression()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PogLangParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(PogLangParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(PogLangParser.PLUS)
            else:
                return self.getToken(PogLangParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(PogLangParser.MINUS)
            else:
                return self.getToken(PogLangParser.MINUS, i)

        def getRuleIndex(self):
            return PogLangParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)




    def additiveExpression(self):

        localctx = PogLangParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.multiplicativeExpression()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 143
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 144
                self.multiplicativeExpression()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PogLangParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(PogLangParser.UnaryExpressionContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(PogLangParser.MULT)
            else:
                return self.getToken(PogLangParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(PogLangParser.DIV)
            else:
                return self.getToken(PogLangParser.DIV, i)

        def getRuleIndex(self):
            return PogLangParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)




    def multiplicativeExpression(self):

        localctx = PogLangParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.unaryExpression()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 151
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 152
                self.unaryExpression()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(PogLangParser.NOT, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(PogLangParser.UnaryExpressionContext,0)


        def primary(self):
            return self.getTypedRuleContext(PogLangParser.PrimaryContext,0)


        def getRuleIndex(self):
            return PogLangParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)




    def unaryExpression(self):

        localctx = PogLangParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_unaryExpression)
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(PogLangParser.NOT)
                self.state = 159
                self.unaryExpression()
                pass
            elif token in [28, 33, 34, 35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PogLangParser.INT, 0)

        def STRING(self):
            return self.getToken(PogLangParser.STRING, 0)

        def ID(self):
            return self.getToken(PogLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(PogLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(PogLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(PogLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return PogLangParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = PogLangParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_primary)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(PogLangParser.INT)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(PogLangParser.STRING)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.match(PogLangParser.ID)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
                self.match(PogLangParser.LPAREN)
                self.state = 167
                self.expression()
                self.state = 168
                self.match(PogLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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




    def type_(self):

        localctx = PogLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
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





