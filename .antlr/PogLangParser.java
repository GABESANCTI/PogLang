// Generated from d:/FACULDADE/Compiladores/poglang shippuden/PogLang/PogLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PogLangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		START=1, END=2, VAL=3, VAR=4, IF=5, ELSE=6, WHILE=7, PRINTLN=8, READLINE=9, 
		POG=10, INT_TYPE=11, STRING_TYPE=12, PLUS=13, MINUS=14, MULT=15, DIV=16, 
		EQUALS=17, NEQUALS=18, LT=19, LTE=20, GT=21, GTE=22, AND=23, OR=24, NOT=25, 
		LBRACE=26, RBRACE=27, LPAREN=28, RPAREN=29, SEMI=30, COLON=31, ASSIGN=32, 
		ID=33, INT=34, STRING=35, WS=36, COMMENT=37;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_expression = 2, RULE_type = 3;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "expression", "type"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'start'", "'end'", "'val'", "'var'", "'if'", "'else'", "'while'", 
			"'println'", "'readLine'", "'pog'", "'Int'", "'String'", "'+'", "'-'", 
			"'*'", "'/'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
			"'!'", "'{'", "'}'", "'('", "')'", "';'", "':'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "START", "END", "VAL", "VAR", "IF", "ELSE", "WHILE", "PRINTLN", 
			"READLINE", "POG", "INT_TYPE", "STRING_TYPE", "PLUS", "MINUS", "MULT", 
			"DIV", "EQUALS", "NEQUALS", "LT", "LTE", "GT", "GTE", "AND", "OR", "NOT", 
			"LBRACE", "RBRACE", "LPAREN", "RPAREN", "SEMI", "COLON", "ASSIGN", "ID", 
			"INT", "STRING", "WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "PogLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PogLangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode START() { return getToken(PogLangParser.START, 0); }
		public TerminalNode LBRACE() { return getToken(PogLangParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(PogLangParser.RBRACE, 0); }
		public TerminalNode END() { return getToken(PogLangParser.END, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(8);
			match(START);
			setState(9);
			match(LBRACE);
			setState(13);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8589936056L) != 0)) {
				{
				{
				setState(10);
				statement();
				}
				}
				setState(15);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(16);
			match(RBRACE);
			setState(17);
			match(END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public TerminalNode VAL() { return getToken(PogLangParser.VAL, 0); }
		public TerminalNode ID() { return getToken(PogLangParser.ID, 0); }
		public TerminalNode COLON() { return getToken(PogLangParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(PogLangParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(PogLangParser.SEMI, 0); }
		public TerminalNode VAR() { return getToken(PogLangParser.VAR, 0); }
		public TerminalNode PRINTLN() { return getToken(PogLangParser.PRINTLN, 0); }
		public TerminalNode LPAREN() { return getToken(PogLangParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(PogLangParser.RPAREN, 0); }
		public TerminalNode READLINE() { return getToken(PogLangParser.READLINE, 0); }
		public TerminalNode IF() { return getToken(PogLangParser.IF, 0); }
		public List<TerminalNode> LBRACE() { return getTokens(PogLangParser.LBRACE); }
		public TerminalNode LBRACE(int i) {
			return getToken(PogLangParser.LBRACE, i);
		}
		public List<TerminalNode> RBRACE() { return getTokens(PogLangParser.RBRACE); }
		public TerminalNode RBRACE(int i) {
			return getToken(PogLangParser.RBRACE, i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(PogLangParser.ELSE, 0); }
		public TerminalNode WHILE() { return getToken(PogLangParser.WHILE, 0); }
		public TerminalNode POG() { return getToken(PogLangParser.POG, 0); }
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		int _la;
		try {
			setState(90);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(19);
				match(VAL);
				setState(20);
				match(ID);
				setState(21);
				match(COLON);
				setState(22);
				type();
				setState(23);
				match(ASSIGN);
				setState(24);
				expression(0);
				setState(25);
				match(SEMI);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(27);
				match(VAR);
				setState(28);
				match(ID);
				setState(29);
				match(COLON);
				setState(30);
				type();
				setState(31);
				match(ASSIGN);
				setState(32);
				expression(0);
				setState(33);
				match(SEMI);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(35);
				match(ID);
				setState(36);
				match(ASSIGN);
				setState(37);
				expression(0);
				setState(38);
				match(SEMI);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(40);
				match(PRINTLN);
				setState(41);
				match(LPAREN);
				setState(42);
				expression(0);
				setState(43);
				match(RPAREN);
				setState(44);
				match(SEMI);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(46);
				match(ID);
				setState(47);
				match(ASSIGN);
				setState(48);
				match(READLINE);
				setState(49);
				match(LPAREN);
				setState(50);
				match(RPAREN);
				setState(51);
				match(SEMI);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(52);
				match(IF);
				setState(53);
				match(LPAREN);
				setState(54);
				expression(0);
				setState(55);
				match(RPAREN);
				setState(56);
				match(LBRACE);
				setState(60);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8589936056L) != 0)) {
					{
					{
					setState(57);
					statement();
					}
					}
					setState(62);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(63);
				match(RBRACE);
				setState(73);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ELSE) {
					{
					setState(64);
					match(ELSE);
					setState(65);
					match(LBRACE);
					setState(69);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8589936056L) != 0)) {
						{
						{
						setState(66);
						statement();
						}
						}
						setState(71);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(72);
					match(RBRACE);
					}
				}

				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(75);
				match(WHILE);
				setState(76);
				match(LPAREN);
				setState(77);
				expression(0);
				setState(78);
				match(RPAREN);
				setState(79);
				match(LBRACE);
				setState(83);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8589936056L) != 0)) {
					{
					{
					setState(80);
					statement();
					}
					}
					setState(85);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(86);
				match(RBRACE);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(88);
				match(POG);
				setState(89);
				match(SEMI);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public Token op;
		public TerminalNode NOT() { return getToken(PogLangParser.NOT, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LPAREN() { return getToken(PogLangParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(PogLangParser.RPAREN, 0); }
		public TerminalNode ID() { return getToken(PogLangParser.ID, 0); }
		public TerminalNode INT() { return getToken(PogLangParser.INT, 0); }
		public TerminalNode STRING() { return getToken(PogLangParser.STRING, 0); }
		public TerminalNode MULT() { return getToken(PogLangParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(PogLangParser.DIV, 0); }
		public TerminalNode PLUS() { return getToken(PogLangParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(PogLangParser.MINUS, 0); }
		public TerminalNode EQUALS() { return getToken(PogLangParser.EQUALS, 0); }
		public TerminalNode NEQUALS() { return getToken(PogLangParser.NEQUALS, 0); }
		public TerminalNode LT() { return getToken(PogLangParser.LT, 0); }
		public TerminalNode LTE() { return getToken(PogLangParser.LTE, 0); }
		public TerminalNode GT() { return getToken(PogLangParser.GT, 0); }
		public TerminalNode GTE() { return getToken(PogLangParser.GTE, 0); }
		public TerminalNode AND() { return getToken(PogLangParser.AND, 0); }
		public TerminalNode OR() { return getToken(PogLangParser.OR, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				{
				setState(93);
				match(NOT);
				setState(94);
				expression(5);
				}
				break;
			case LPAREN:
				{
				setState(95);
				match(LPAREN);
				setState(96);
				expression(0);
				setState(97);
				match(RPAREN);
				}
				break;
			case ID:
				{
				setState(99);
				match(ID);
				}
				break;
			case INT:
				{
				setState(100);
				match(INT);
				}
				break;
			case STRING:
				{
				setState(101);
				match(STRING);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(118);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(116);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(104);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(105);
						((ExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MULT || _la==DIV) ) {
							((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(106);
						expression(10);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(107);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(108);
						((ExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
							((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(109);
						expression(9);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(110);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(111);
						((ExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 8257536L) != 0)) ) {
							((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(112);
						expression(8);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(113);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(114);
						((ExpressionContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==AND || _la==OR) ) {
							((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(115);
						expression(7);
						}
						break;
					}
					} 
				}
				setState(120);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TerminalNode INT_TYPE() { return getToken(PogLangParser.INT_TYPE, 0); }
		public TerminalNode STRING_TYPE() { return getToken(PogLangParser.STRING_TYPE, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			_la = _input.LA(1);
			if ( !(_la==INT_TYPE || _la==STRING_TYPE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 9);
		case 1:
			return precpred(_ctx, 8);
		case 2:
			return precpred(_ctx, 7);
		case 3:
			return precpred(_ctx, 6);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001%|\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002\u0002"+
		"\u0007\u0002\u0002\u0003\u0007\u0003\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0005\u0000\f\b\u0000\n\u0000\f\u0000\u000f\t\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001;\b"+
		"\u0001\n\u0001\f\u0001>\t\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0005\u0001D\b\u0001\n\u0001\f\u0001G\t\u0001\u0001\u0001\u0003"+
		"\u0001J\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0005\u0001R\b\u0001\n\u0001\f\u0001U\t\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001[\b\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002g\b\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005"+
		"\u0002u\b\u0002\n\u0002\f\u0002x\t\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0000\u0001\u0004\u0004\u0000\u0002\u0004\u0006\u0000\u0005\u0001"+
		"\u0000\u000f\u0010\u0001\u0000\r\u000e\u0001\u0000\u0011\u0016\u0001\u0000"+
		"\u0017\u0018\u0001\u0000\u000b\f\u008b\u0000\b\u0001\u0000\u0000\u0000"+
		"\u0002Z\u0001\u0000\u0000\u0000\u0004f\u0001\u0000\u0000\u0000\u0006y"+
		"\u0001\u0000\u0000\u0000\b\t\u0005\u0001\u0000\u0000\t\r\u0005\u001a\u0000"+
		"\u0000\n\f\u0003\u0002\u0001\u0000\u000b\n\u0001\u0000\u0000\u0000\f\u000f"+
		"\u0001\u0000\u0000\u0000\r\u000b\u0001\u0000\u0000\u0000\r\u000e\u0001"+
		"\u0000\u0000\u0000\u000e\u0010\u0001\u0000\u0000\u0000\u000f\r\u0001\u0000"+
		"\u0000\u0000\u0010\u0011\u0005\u001b\u0000\u0000\u0011\u0012\u0005\u0002"+
		"\u0000\u0000\u0012\u0001\u0001\u0000\u0000\u0000\u0013\u0014\u0005\u0003"+
		"\u0000\u0000\u0014\u0015\u0005!\u0000\u0000\u0015\u0016\u0005\u001f\u0000"+
		"\u0000\u0016\u0017\u0003\u0006\u0003\u0000\u0017\u0018\u0005 \u0000\u0000"+
		"\u0018\u0019\u0003\u0004\u0002\u0000\u0019\u001a\u0005\u001e\u0000\u0000"+
		"\u001a[\u0001\u0000\u0000\u0000\u001b\u001c\u0005\u0004\u0000\u0000\u001c"+
		"\u001d\u0005!\u0000\u0000\u001d\u001e\u0005\u001f\u0000\u0000\u001e\u001f"+
		"\u0003\u0006\u0003\u0000\u001f \u0005 \u0000\u0000 !\u0003\u0004\u0002"+
		"\u0000!\"\u0005\u001e\u0000\u0000\"[\u0001\u0000\u0000\u0000#$\u0005!"+
		"\u0000\u0000$%\u0005 \u0000\u0000%&\u0003\u0004\u0002\u0000&\'\u0005\u001e"+
		"\u0000\u0000\'[\u0001\u0000\u0000\u0000()\u0005\b\u0000\u0000)*\u0005"+
		"\u001c\u0000\u0000*+\u0003\u0004\u0002\u0000+,\u0005\u001d\u0000\u0000"+
		",-\u0005\u001e\u0000\u0000-[\u0001\u0000\u0000\u0000./\u0005!\u0000\u0000"+
		"/0\u0005 \u0000\u000001\u0005\t\u0000\u000012\u0005\u001c\u0000\u0000"+
		"23\u0005\u001d\u0000\u00003[\u0005\u001e\u0000\u000045\u0005\u0005\u0000"+
		"\u000056\u0005\u001c\u0000\u000067\u0003\u0004\u0002\u000078\u0005\u001d"+
		"\u0000\u00008<\u0005\u001a\u0000\u00009;\u0003\u0002\u0001\u0000:9\u0001"+
		"\u0000\u0000\u0000;>\u0001\u0000\u0000\u0000<:\u0001\u0000\u0000\u0000"+
		"<=\u0001\u0000\u0000\u0000=?\u0001\u0000\u0000\u0000><\u0001\u0000\u0000"+
		"\u0000?I\u0005\u001b\u0000\u0000@A\u0005\u0006\u0000\u0000AE\u0005\u001a"+
		"\u0000\u0000BD\u0003\u0002\u0001\u0000CB\u0001\u0000\u0000\u0000DG\u0001"+
		"\u0000\u0000\u0000EC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000"+
		"FH\u0001\u0000\u0000\u0000GE\u0001\u0000\u0000\u0000HJ\u0005\u001b\u0000"+
		"\u0000I@\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000J[\u0001\u0000"+
		"\u0000\u0000KL\u0005\u0007\u0000\u0000LM\u0005\u001c\u0000\u0000MN\u0003"+
		"\u0004\u0002\u0000NO\u0005\u001d\u0000\u0000OS\u0005\u001a\u0000\u0000"+
		"PR\u0003\u0002\u0001\u0000QP\u0001\u0000\u0000\u0000RU\u0001\u0000\u0000"+
		"\u0000SQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000TV\u0001\u0000"+
		"\u0000\u0000US\u0001\u0000\u0000\u0000VW\u0005\u001b\u0000\u0000W[\u0001"+
		"\u0000\u0000\u0000XY\u0005\n\u0000\u0000Y[\u0005\u001e\u0000\u0000Z\u0013"+
		"\u0001\u0000\u0000\u0000Z\u001b\u0001\u0000\u0000\u0000Z#\u0001\u0000"+
		"\u0000\u0000Z(\u0001\u0000\u0000\u0000Z.\u0001\u0000\u0000\u0000Z4\u0001"+
		"\u0000\u0000\u0000ZK\u0001\u0000\u0000\u0000ZX\u0001\u0000\u0000\u0000"+
		"[\u0003\u0001\u0000\u0000\u0000\\]\u0006\u0002\uffff\uffff\u0000]^\u0005"+
		"\u0019\u0000\u0000^g\u0003\u0004\u0002\u0005_`\u0005\u001c\u0000\u0000"+
		"`a\u0003\u0004\u0002\u0000ab\u0005\u001d\u0000\u0000bg\u0001\u0000\u0000"+
		"\u0000cg\u0005!\u0000\u0000dg\u0005\"\u0000\u0000eg\u0005#\u0000\u0000"+
		"f\\\u0001\u0000\u0000\u0000f_\u0001\u0000\u0000\u0000fc\u0001\u0000\u0000"+
		"\u0000fd\u0001\u0000\u0000\u0000fe\u0001\u0000\u0000\u0000gv\u0001\u0000"+
		"\u0000\u0000hi\n\t\u0000\u0000ij\u0007\u0000\u0000\u0000ju\u0003\u0004"+
		"\u0002\nkl\n\b\u0000\u0000lm\u0007\u0001\u0000\u0000mu\u0003\u0004\u0002"+
		"\tno\n\u0007\u0000\u0000op\u0007\u0002\u0000\u0000pu\u0003\u0004\u0002"+
		"\bqr\n\u0006\u0000\u0000rs\u0007\u0003\u0000\u0000su\u0003\u0004\u0002"+
		"\u0007th\u0001\u0000\u0000\u0000tk\u0001\u0000\u0000\u0000tn\u0001\u0000"+
		"\u0000\u0000tq\u0001\u0000\u0000\u0000ux\u0001\u0000\u0000\u0000vt\u0001"+
		"\u0000\u0000\u0000vw\u0001\u0000\u0000\u0000w\u0005\u0001\u0000\u0000"+
		"\u0000xv\u0001\u0000\u0000\u0000yz\u0007\u0004\u0000\u0000z\u0007\u0001"+
		"\u0000\u0000\u0000\t\r<EISZftv";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}