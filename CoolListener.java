// Generated from Cool.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CoolParser}.
 */
public interface CoolListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by the {@code Programa}
	 * labeled alternative in {@link CoolParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(CoolParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Programa}
	 * labeled alternative in {@link CoolParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(CoolParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Classe}
	 * labeled alternative in {@link CoolParser#class}.
	 * @param ctx the parse tree
	 */
	void enterClasse(CoolParser.ClasseContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Classe}
	 * labeled alternative in {@link CoolParser#class}.
	 * @param ctx the parse tree
	 */
	void exitClasse(CoolParser.ClasseContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Metodo}
	 * labeled alternative in {@link CoolParser#feature}.
	 * @param ctx the parse tree
	 */
	void enterMetodo(CoolParser.MetodoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Metodo}
	 * labeled alternative in {@link CoolParser#feature}.
	 * @param ctx the parse tree
	 */
	void exitMetodo(CoolParser.MetodoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DeclaracaoFeature}
	 * labeled alternative in {@link CoolParser#feature}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracaoFeature(CoolParser.DeclaracaoFeatureContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DeclaracaoFeature}
	 * labeled alternative in {@link CoolParser#feature}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracaoFeature(CoolParser.DeclaracaoFeatureContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DeclaracaoFormal}
	 * labeled alternative in {@link CoolParser#formal}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracaoFormal(CoolParser.DeclaracaoFormalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DeclaracaoFormal}
	 * labeled alternative in {@link CoolParser#formal}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracaoFormal(CoolParser.DeclaracaoFormalContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MenorIgual}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMenorIgual(CoolParser.MenorIgualContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MenorIgual}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMenorIgual(CoolParser.MenorIgualContext ctx);
	/**
	 * Enter a parse tree produced by the {@code VariasExpr}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterVariasExpr(CoolParser.VariasExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code VariasExpr}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitVariasExpr(CoolParser.VariasExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NegacaoNot}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNegacaoNot(CoolParser.NegacaoNotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NegacaoNot}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNegacaoNot(CoolParser.NegacaoNotContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Falso}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterFalso(CoolParser.FalsoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Falso}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitFalso(CoolParser.FalsoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code String}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterString(CoolParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code String}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitString(CoolParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Subtracao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterSubtracao(CoolParser.SubtracaoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Subtracao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitSubtracao(CoolParser.SubtracaoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Divisao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterDivisao(CoolParser.DivisaoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Divisao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitDivisao(CoolParser.DivisaoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Case}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterCase(CoolParser.CaseContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Case}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitCase(CoolParser.CaseContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Verdadeiro}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterVerdadeiro(CoolParser.VerdadeiroContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Verdadeiro}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitVerdadeiro(CoolParser.VerdadeiroContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Adicao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAdicao(CoolParser.AdicaoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Adicao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAdicao(CoolParser.AdicaoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Igual}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIgual(CoolParser.IgualContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Igual}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIgual(CoolParser.IgualContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprChaves}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExprChaves(CoolParser.ExprChavesContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprChaves}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExprChaves(CoolParser.ExprChavesContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Negacao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNegacao(CoolParser.NegacaoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Negacao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNegacao(CoolParser.NegacaoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Atribuicao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAtribuicao(CoolParser.AtribuicaoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Atribuicao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAtribuicao(CoolParser.AtribuicaoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ENulo}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterENulo(CoolParser.ENuloContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ENulo}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitENulo(CoolParser.ENuloContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Inteiro}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterInteiro(CoolParser.InteiroContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Inteiro}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitInteiro(CoolParser.InteiroContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Loop}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLoop(CoolParser.LoopContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Loop}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLoop(CoolParser.LoopContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Multiplicacao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicacao(CoolParser.MultiplicacaoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Multiplicacao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicacao(CoolParser.MultiplicacaoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NovoTipo}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNovoTipo(CoolParser.NovoTipoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NovoTipo}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNovoTipo(CoolParser.NovoTipoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprArroba}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExprArroba(CoolParser.ExprArrobaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprArroba}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExprArroba(CoolParser.ExprArrobaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Menor}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMenor(CoolParser.MenorContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Menor}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMenor(CoolParser.MenorContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Let}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLet(CoolParser.LetContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Let}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLet(CoolParser.LetContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Identificador}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIdentificador(CoolParser.IdentificadorContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Identificador}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIdentificador(CoolParser.IdentificadorContext ctx);
	/**
	 * Enter a parse tree produced by the {@code If}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIf(CoolParser.IfContext ctx);
	/**
	 * Exit a parse tree produced by the {@code If}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIf(CoolParser.IfContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprParenteses}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExprParenteses(CoolParser.ExprParentesesContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprParenteses}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExprParenteses(CoolParser.ExprParentesesContext ctx);
}