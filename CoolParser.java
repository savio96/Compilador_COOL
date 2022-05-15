// Generated from Cool.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CoolParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		ID=39, TYPE=40, STRING=41, INTEGER=42, WS=43, LINE_COMMENT=44, COMMENT=45;
	public static final int
		RULE_prog = 0, RULE_class = 1, RULE_feature = 2, RULE_formal = 3, RULE_expr = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "class", "feature", "formal", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'class'", "'inherits'", "'{'", "'}'", "'('", "','", "')'", 
			"':'", "'<-'", "'@'", "'.'", "'if'", "'then'", "'else'", "'fi'", "'while'", 
			"'loop'", "'pool'", "'let'", "'in'", "'case'", "'of'", "'=>'", "'esac'", 
			"'new'", "'isvoid'", "'+'", "'-'", "'*'", "'/'", "'~'", "'<'", "'<='", 
			"'='", "'not'", "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "ID", "TYPE", "STRING", "INTEGER", "WS", "LINE_COMMENT", 
			"COMMENT"
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
	public String getGrammarFileName() { return "Cool.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CoolParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public List<ClassContext> class_() {
			return getRuleContexts(ClassContext.class);
		}
		public ClassContext class_(int i) {
			return getRuleContext(ClassContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoolListener ) ((CoolListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoolListener ) ((CoolListener)listener).exitProg(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(10);
				class_();
				setState(11);
				match(T__0);
				}
				}
				setState(15); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__1 );
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

	public static class ClassContext extends ParserRuleContext {
		public List<TerminalNode> TYPE() { return getTokens(CoolParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(CoolParser.TYPE, i);
		}
		public List<FeatureContext> feature() {
			return getRuleContexts(FeatureContext.class);
		}
		public FeatureContext feature(int i) {
			return getRuleContext(FeatureContext.class,i);
		}
		public ClassContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoolListener ) ((CoolListener)listener).enterClass(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoolListener ) ((CoolListener)listener).exitClass(this);
		}
	}

	public final ClassContext class_() throws RecognitionException {
		ClassContext _localctx = new ClassContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_class);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(17);
			match(T__1);
			setState(18);
			match(TYPE);
			setState(21);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2) {
				{
				setState(19);
				match(T__2);
				setState(20);
				match(TYPE);
				}
			}

			setState(23);
			match(T__3);
			setState(29);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(24);
				feature();
				setState(25);
				match(T__0);
				}
				}
				setState(31);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(32);
			match(T__4);
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

	public static class FeatureContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CoolParser.ID, 0); }
		public TerminalNode TYPE() { return getToken(CoolParser.TYPE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<FormalContext> formal() {
			return getRuleContexts(FormalContext.class);
		}
		public FormalContext formal(int i) {
			return getRuleContext(FormalContext.class,i);
		}
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoolListener ) ((CoolListener)listener).enterFeature(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoolListener ) ((CoolListener)listener).exitFeature(this);
		}
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_feature);
		int _la;
		try {
			setState(60);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(34);
				match(ID);
				setState(35);
				match(T__5);
				setState(44);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(36);
					formal();
					setState(41);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__6) {
						{
						{
						setState(37);
						match(T__6);
						setState(38);
						formal();
						}
						}
						setState(43);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(46);
				match(T__7);
				setState(47);
				match(T__8);
				setState(48);
				match(TYPE);
				setState(49);
				match(T__3);
				setState(50);
				expr(0);
				setState(51);
				match(T__4);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(53);
				match(ID);
				setState(54);
				match(T__8);
				setState(55);
				match(TYPE);
				setState(58);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__9) {
					{
					setState(56);
					match(T__9);
					setState(57);
					expr(0);
					}
				}

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

	public static class FormalContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CoolParser.ID, 0); }
		public TerminalNode TYPE() { return getToken(CoolParser.TYPE, 0); }
		public FormalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoolListener ) ((CoolListener)listener).enterFormal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoolListener ) ((CoolListener)listener).exitFormal(this);
		}
	}

	public final FormalContext formal() throws RecognitionException {
		FormalContext _localctx = new FormalContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_formal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			match(ID);
			setState(63);
			match(T__8);
			setState(64);
			match(TYPE);
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

	public static class ExprContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(CoolParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(CoolParser.ID, i);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> TYPE() { return getTokens(CoolParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(CoolParser.TYPE, i);
		}
		public TerminalNode INTEGER() { return getToken(CoolParser.INTEGER, 0); }
		public TerminalNode STRING() { return getToken(CoolParser.STRING, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoolListener ) ((CoolListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoolListener ) ((CoolListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(67);
				match(ID);
				setState(68);
				match(T__9);
				setState(69);
				expr(25);
				}
				break;
			case 2:
				{
				setState(70);
				match(ID);
				setState(71);
				match(T__5);
				setState(80);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__3) | (1L << T__5) | (1L << T__12) | (1L << T__16) | (1L << T__19) | (1L << T__21) | (1L << T__25) | (1L << T__26) | (1L << T__31) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << ID) | (1L << STRING) | (1L << INTEGER))) != 0)) {
					{
					setState(72);
					expr(0);
					setState(77);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__6) {
						{
						{
						setState(73);
						match(T__6);
						setState(74);
						expr(0);
						}
						}
						setState(79);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(82);
				match(T__7);
				}
				break;
			case 3:
				{
				setState(83);
				match(T__12);
				setState(84);
				expr(0);
				setState(85);
				match(T__13);
				setState(86);
				expr(0);
				setState(87);
				match(T__14);
				setState(88);
				expr(0);
				setState(89);
				match(T__15);
				}
				break;
			case 4:
				{
				setState(91);
				match(T__16);
				setState(92);
				expr(0);
				setState(93);
				match(T__17);
				setState(94);
				expr(0);
				setState(95);
				match(T__18);
				}
				break;
			case 5:
				{
				setState(97);
				match(T__3);
				setState(101); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(98);
					expr(0);
					setState(99);
					match(T__0);
					}
					}
					setState(103); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__3) | (1L << T__5) | (1L << T__12) | (1L << T__16) | (1L << T__19) | (1L << T__21) | (1L << T__25) | (1L << T__26) | (1L << T__31) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << ID) | (1L << STRING) | (1L << INTEGER))) != 0) );
				setState(105);
				match(T__4);
				}
				break;
			case 6:
				{
				setState(107);
				match(T__19);
				setState(108);
				match(ID);
				setState(109);
				match(T__8);
				setState(110);
				match(TYPE);
				setState(113);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__9) {
					{
					setState(111);
					match(T__9);
					setState(112);
					expr(0);
					}
				}

				setState(125);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__6) {
					{
					{
					setState(115);
					match(T__6);
					setState(116);
					match(ID);
					setState(117);
					match(T__8);
					setState(118);
					match(TYPE);
					setState(121);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__9) {
						{
						setState(119);
						match(T__9);
						setState(120);
						expr(0);
						}
					}

					}
					}
					setState(127);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(128);
				match(T__20);
				setState(129);
				expr(19);
				}
				break;
			case 7:
				{
				setState(130);
				match(T__21);
				setState(131);
				expr(0);
				setState(132);
				match(T__22);
				setState(138); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(133);
					match(ID);
					setState(134);
					match(T__8);
					setState(135);
					match(TYPE);
					setState(136);
					match(T__23);
					setState(137);
					expr(0);
					}
					}
					setState(140); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==ID );
				setState(142);
				match(T__24);
				}
				break;
			case 8:
				{
				setState(144);
				match(T__25);
				setState(145);
				match(TYPE);
				}
				break;
			case 9:
				{
				setState(146);
				match(T__26);
				setState(147);
				expr(16);
				}
				break;
			case 10:
				{
				setState(148);
				match(T__31);
				setState(149);
				expr(11);
				}
				break;
			case 11:
				{
				setState(150);
				match(T__35);
				setState(151);
				expr(7);
				}
				break;
			case 12:
				{
				setState(152);
				match(T__5);
				setState(153);
				expr(0);
				setState(154);
				match(T__7);
				}
				break;
			case 13:
				{
				setState(156);
				match(ID);
				}
				break;
			case 14:
				{
				setState(157);
				match(INTEGER);
				}
				break;
			case 15:
				{
				setState(158);
				match(STRING);
				}
				break;
			case 16:
				{
				setState(159);
				match(T__36);
				}
				break;
			case 17:
				{
				setState(160);
				match(T__37);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(205);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(203);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(163);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(164);
						match(T__27);
						setState(165);
						expr(16);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(166);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(167);
						match(T__28);
						setState(168);
						expr(15);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(169);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(170);
						match(T__29);
						setState(171);
						expr(14);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(172);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(173);
						match(T__30);
						setState(174);
						expr(13);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(175);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(176);
						match(T__32);
						setState(177);
						expr(11);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(178);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(179);
						match(T__33);
						setState(180);
						expr(10);
						}
						break;
					case 7:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(181);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(182);
						match(T__34);
						setState(183);
						expr(9);
						}
						break;
					case 8:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(184);
						if (!(precpred(_ctx, 24))) throw new FailedPredicateException(this, "precpred(_ctx, 24)");
						setState(187);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==T__10) {
							{
							setState(185);
							match(T__10);
							setState(186);
							match(TYPE);
							}
						}

						setState(189);
						match(T__11);
						setState(190);
						match(ID);
						setState(191);
						match(T__5);
						setState(200);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__3) | (1L << T__5) | (1L << T__12) | (1L << T__16) | (1L << T__19) | (1L << T__21) | (1L << T__25) | (1L << T__26) | (1L << T__31) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << ID) | (1L << STRING) | (1L << INTEGER))) != 0)) {
							{
							setState(192);
							expr(0);
							setState(197);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==T__6) {
								{
								{
								setState(193);
								match(T__6);
								setState(194);
								expr(0);
								}
								}
								setState(199);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(202);
						match(T__7);
						}
						break;
					}
					} 
				}
				setState(207);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 15);
		case 1:
			return precpred(_ctx, 14);
		case 2:
			return precpred(_ctx, 13);
		case 3:
			return precpred(_ctx, 12);
		case 4:
			return precpred(_ctx, 10);
		case 5:
			return precpred(_ctx, 9);
		case 6:
			return precpred(_ctx, 8);
		case 7:
			return precpred(_ctx, 24);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001-\u00d1\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0004\u0000\u000e\b\u0000\u000b\u0000\f"+
		"\u0000\u000f\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"\u0016\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001"+
		"\u001c\b\u0001\n\u0001\f\u0001\u001f\t\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002(\b"+
		"\u0002\n\u0002\f\u0002+\t\u0002\u0003\u0002-\b\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002;\b"+
		"\u0002\u0003\u0002=\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004L\b\u0004\n\u0004"+
		"\f\u0004O\t\u0004\u0003\u0004Q\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0004\u0004f\b\u0004"+
		"\u000b\u0004\f\u0004g\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004r\b\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0003\u0004z\b\u0004\u0005\u0004|\b\u0004\n\u0004\f\u0004\u007f\t\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0004\u0004\u008b\b\u0004"+
		"\u000b\u0004\f\u0004\u008c\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u00a2\b\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004"+
		"\u00bc\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0005\u0004\u00c4\b\u0004\n\u0004\f\u0004\u00c7\t\u0004\u0003"+
		"\u0004\u00c9\b\u0004\u0001\u0004\u0005\u0004\u00cc\b\u0004\n\u0004\f\u0004"+
		"\u00cf\t\u0004\u0001\u0004\u0000\u0001\b\u0005\u0000\u0002\u0004\u0006"+
		"\b\u0000\u0000\u00f4\u0000\r\u0001\u0000\u0000\u0000\u0002\u0011\u0001"+
		"\u0000\u0000\u0000\u0004<\u0001\u0000\u0000\u0000\u0006>\u0001\u0000\u0000"+
		"\u0000\b\u00a1\u0001\u0000\u0000\u0000\n\u000b\u0003\u0002\u0001\u0000"+
		"\u000b\f\u0005\u0001\u0000\u0000\f\u000e\u0001\u0000\u0000\u0000\r\n\u0001"+
		"\u0000\u0000\u0000\u000e\u000f\u0001\u0000\u0000\u0000\u000f\r\u0001\u0000"+
		"\u0000\u0000\u000f\u0010\u0001\u0000\u0000\u0000\u0010\u0001\u0001\u0000"+
		"\u0000\u0000\u0011\u0012\u0005\u0002\u0000\u0000\u0012\u0015\u0005(\u0000"+
		"\u0000\u0013\u0014\u0005\u0003\u0000\u0000\u0014\u0016\u0005(\u0000\u0000"+
		"\u0015\u0013\u0001\u0000\u0000\u0000\u0015\u0016\u0001\u0000\u0000\u0000"+
		"\u0016\u0017\u0001\u0000\u0000\u0000\u0017\u001d\u0005\u0004\u0000\u0000"+
		"\u0018\u0019\u0003\u0004\u0002\u0000\u0019\u001a\u0005\u0001\u0000\u0000"+
		"\u001a\u001c\u0001\u0000\u0000\u0000\u001b\u0018\u0001\u0000\u0000\u0000"+
		"\u001c\u001f\u0001\u0000\u0000\u0000\u001d\u001b\u0001\u0000\u0000\u0000"+
		"\u001d\u001e\u0001\u0000\u0000\u0000\u001e \u0001\u0000\u0000\u0000\u001f"+
		"\u001d\u0001\u0000\u0000\u0000 !\u0005\u0005\u0000\u0000!\u0003\u0001"+
		"\u0000\u0000\u0000\"#\u0005\'\u0000\u0000#,\u0005\u0006\u0000\u0000$)"+
		"\u0003\u0006\u0003\u0000%&\u0005\u0007\u0000\u0000&(\u0003\u0006\u0003"+
		"\u0000\'%\u0001\u0000\u0000\u0000(+\u0001\u0000\u0000\u0000)\'\u0001\u0000"+
		"\u0000\u0000)*\u0001\u0000\u0000\u0000*-\u0001\u0000\u0000\u0000+)\u0001"+
		"\u0000\u0000\u0000,$\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000"+
		"-.\u0001\u0000\u0000\u0000./\u0005\b\u0000\u0000/0\u0005\t\u0000\u0000"+
		"01\u0005(\u0000\u000012\u0005\u0004\u0000\u000023\u0003\b\u0004\u0000"+
		"34\u0005\u0005\u0000\u00004=\u0001\u0000\u0000\u000056\u0005\'\u0000\u0000"+
		"67\u0005\t\u0000\u00007:\u0005(\u0000\u000089\u0005\n\u0000\u00009;\u0003"+
		"\b\u0004\u0000:8\u0001\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000;=\u0001"+
		"\u0000\u0000\u0000<\"\u0001\u0000\u0000\u0000<5\u0001\u0000\u0000\u0000"+
		"=\u0005\u0001\u0000\u0000\u0000>?\u0005\'\u0000\u0000?@\u0005\t\u0000"+
		"\u0000@A\u0005(\u0000\u0000A\u0007\u0001\u0000\u0000\u0000BC\u0006\u0004"+
		"\uffff\uffff\u0000CD\u0005\'\u0000\u0000DE\u0005\n\u0000\u0000E\u00a2"+
		"\u0003\b\u0004\u0019FG\u0005\'\u0000\u0000GP\u0005\u0006\u0000\u0000H"+
		"M\u0003\b\u0004\u0000IJ\u0005\u0007\u0000\u0000JL\u0003\b\u0004\u0000"+
		"KI\u0001\u0000\u0000\u0000LO\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000"+
		"\u0000MN\u0001\u0000\u0000\u0000NQ\u0001\u0000\u0000\u0000OM\u0001\u0000"+
		"\u0000\u0000PH\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000QR\u0001"+
		"\u0000\u0000\u0000R\u00a2\u0005\b\u0000\u0000ST\u0005\r\u0000\u0000TU"+
		"\u0003\b\u0004\u0000UV\u0005\u000e\u0000\u0000VW\u0003\b\u0004\u0000W"+
		"X\u0005\u000f\u0000\u0000XY\u0003\b\u0004\u0000YZ\u0005\u0010\u0000\u0000"+
		"Z\u00a2\u0001\u0000\u0000\u0000[\\\u0005\u0011\u0000\u0000\\]\u0003\b"+
		"\u0004\u0000]^\u0005\u0012\u0000\u0000^_\u0003\b\u0004\u0000_`\u0005\u0013"+
		"\u0000\u0000`\u00a2\u0001\u0000\u0000\u0000ae\u0005\u0004\u0000\u0000"+
		"bc\u0003\b\u0004\u0000cd\u0005\u0001\u0000\u0000df\u0001\u0000\u0000\u0000"+
		"eb\u0001\u0000\u0000\u0000fg\u0001\u0000\u0000\u0000ge\u0001\u0000\u0000"+
		"\u0000gh\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000ij\u0005\u0005"+
		"\u0000\u0000j\u00a2\u0001\u0000\u0000\u0000kl\u0005\u0014\u0000\u0000"+
		"lm\u0005\'\u0000\u0000mn\u0005\t\u0000\u0000nq\u0005(\u0000\u0000op\u0005"+
		"\n\u0000\u0000pr\u0003\b\u0004\u0000qo\u0001\u0000\u0000\u0000qr\u0001"+
		"\u0000\u0000\u0000r}\u0001\u0000\u0000\u0000st\u0005\u0007\u0000\u0000"+
		"tu\u0005\'\u0000\u0000uv\u0005\t\u0000\u0000vy\u0005(\u0000\u0000wx\u0005"+
		"\n\u0000\u0000xz\u0003\b\u0004\u0000yw\u0001\u0000\u0000\u0000yz\u0001"+
		"\u0000\u0000\u0000z|\u0001\u0000\u0000\u0000{s\u0001\u0000\u0000\u0000"+
		"|\u007f\u0001\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000}~\u0001\u0000"+
		"\u0000\u0000~\u0080\u0001\u0000\u0000\u0000\u007f}\u0001\u0000\u0000\u0000"+
		"\u0080\u0081\u0005\u0015\u0000\u0000\u0081\u00a2\u0003\b\u0004\u0013\u0082"+
		"\u0083\u0005\u0016\u0000\u0000\u0083\u0084\u0003\b\u0004\u0000\u0084\u008a"+
		"\u0005\u0017\u0000\u0000\u0085\u0086\u0005\'\u0000\u0000\u0086\u0087\u0005"+
		"\t\u0000\u0000\u0087\u0088\u0005(\u0000\u0000\u0088\u0089\u0005\u0018"+
		"\u0000\u0000\u0089\u008b\u0003\b\u0004\u0000\u008a\u0085\u0001\u0000\u0000"+
		"\u0000\u008b\u008c\u0001\u0000\u0000\u0000\u008c\u008a\u0001\u0000\u0000"+
		"\u0000\u008c\u008d\u0001\u0000\u0000\u0000\u008d\u008e\u0001\u0000\u0000"+
		"\u0000\u008e\u008f\u0005\u0019\u0000\u0000\u008f\u00a2\u0001\u0000\u0000"+
		"\u0000\u0090\u0091\u0005\u001a\u0000\u0000\u0091\u00a2\u0005(\u0000\u0000"+
		"\u0092\u0093\u0005\u001b\u0000\u0000\u0093\u00a2\u0003\b\u0004\u0010\u0094"+
		"\u0095\u0005 \u0000\u0000\u0095\u00a2\u0003\b\u0004\u000b\u0096\u0097"+
		"\u0005$\u0000\u0000\u0097\u00a2\u0003\b\u0004\u0007\u0098\u0099\u0005"+
		"\u0006\u0000\u0000\u0099\u009a\u0003\b\u0004\u0000\u009a\u009b\u0005\b"+
		"\u0000\u0000\u009b\u00a2\u0001\u0000\u0000\u0000\u009c\u00a2\u0005\'\u0000"+
		"\u0000\u009d\u00a2\u0005*\u0000\u0000\u009e\u00a2\u0005)\u0000\u0000\u009f"+
		"\u00a2\u0005%\u0000\u0000\u00a0\u00a2\u0005&\u0000\u0000\u00a1B\u0001"+
		"\u0000\u0000\u0000\u00a1F\u0001\u0000\u0000\u0000\u00a1S\u0001\u0000\u0000"+
		"\u0000\u00a1[\u0001\u0000\u0000\u0000\u00a1a\u0001\u0000\u0000\u0000\u00a1"+
		"k\u0001\u0000\u0000\u0000\u00a1\u0082\u0001\u0000\u0000\u0000\u00a1\u0090"+
		"\u0001\u0000\u0000\u0000\u00a1\u0092\u0001\u0000\u0000\u0000\u00a1\u0094"+
		"\u0001\u0000\u0000\u0000\u00a1\u0096\u0001\u0000\u0000\u0000\u00a1\u0098"+
		"\u0001\u0000\u0000\u0000\u00a1\u009c\u0001\u0000\u0000\u0000\u00a1\u009d"+
		"\u0001\u0000\u0000\u0000\u00a1\u009e\u0001\u0000\u0000\u0000\u00a1\u009f"+
		"\u0001\u0000\u0000\u0000\u00a1\u00a0\u0001\u0000\u0000\u0000\u00a2\u00cd"+
		"\u0001\u0000\u0000\u0000\u00a3\u00a4\n\u000f\u0000\u0000\u00a4\u00a5\u0005"+
		"\u001c\u0000\u0000\u00a5\u00cc\u0003\b\u0004\u0010\u00a6\u00a7\n\u000e"+
		"\u0000\u0000\u00a7\u00a8\u0005\u001d\u0000\u0000\u00a8\u00cc\u0003\b\u0004"+
		"\u000f\u00a9\u00aa\n\r\u0000\u0000\u00aa\u00ab\u0005\u001e\u0000\u0000"+
		"\u00ab\u00cc\u0003\b\u0004\u000e\u00ac\u00ad\n\f\u0000\u0000\u00ad\u00ae"+
		"\u0005\u001f\u0000\u0000\u00ae\u00cc\u0003\b\u0004\r\u00af\u00b0\n\n\u0000"+
		"\u0000\u00b0\u00b1\u0005!\u0000\u0000\u00b1\u00cc\u0003\b\u0004\u000b"+
		"\u00b2\u00b3\n\t\u0000\u0000\u00b3\u00b4\u0005\"\u0000\u0000\u00b4\u00cc"+
		"\u0003\b\u0004\n\u00b5\u00b6\n\b\u0000\u0000\u00b6\u00b7\u0005#\u0000"+
		"\u0000\u00b7\u00cc\u0003\b\u0004\t\u00b8\u00bb\n\u0018\u0000\u0000\u00b9"+
		"\u00ba\u0005\u000b\u0000\u0000\u00ba\u00bc\u0005(\u0000\u0000\u00bb\u00b9"+
		"\u0001\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc\u00bd"+
		"\u0001\u0000\u0000\u0000\u00bd\u00be\u0005\f\u0000\u0000\u00be\u00bf\u0005"+
		"\'\u0000\u0000\u00bf\u00c8\u0005\u0006\u0000\u0000\u00c0\u00c5\u0003\b"+
		"\u0004\u0000\u00c1\u00c2\u0005\u0007\u0000\u0000\u00c2\u00c4\u0003\b\u0004"+
		"\u0000\u00c3\u00c1\u0001\u0000\u0000\u0000\u00c4\u00c7\u0001\u0000\u0000"+
		"\u0000\u00c5\u00c3\u0001\u0000\u0000\u0000\u00c5\u00c6\u0001\u0000\u0000"+
		"\u0000\u00c6\u00c9\u0001\u0000\u0000\u0000\u00c7\u00c5\u0001\u0000\u0000"+
		"\u0000\u00c8\u00c0\u0001\u0000\u0000\u0000\u00c8\u00c9\u0001\u0000\u0000"+
		"\u0000\u00c9\u00ca\u0001\u0000\u0000\u0000\u00ca\u00cc\u0005\b\u0000\u0000"+
		"\u00cb\u00a3\u0001\u0000\u0000\u0000\u00cb\u00a6\u0001\u0000\u0000\u0000"+
		"\u00cb\u00a9\u0001\u0000\u0000\u0000\u00cb\u00ac\u0001\u0000\u0000\u0000"+
		"\u00cb\u00af\u0001\u0000\u0000\u0000\u00cb\u00b2\u0001\u0000\u0000\u0000"+
		"\u00cb\u00b5\u0001\u0000\u0000\u0000\u00cb\u00b8\u0001\u0000\u0000\u0000"+
		"\u00cc\u00cf\u0001\u0000\u0000\u0000\u00cd\u00cb\u0001\u0000\u0000\u0000"+
		"\u00cd\u00ce\u0001\u0000\u0000\u0000\u00ce\t\u0001\u0000\u0000\u0000\u00cf"+
		"\u00cd\u0001\u0000\u0000\u0000\u0014\u000f\u0015\u001d),:<MPgqy}\u008c"+
		"\u00a1\u00bb\u00c5\u00c8\u00cb\u00cd";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}