// Generated from Cool.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link CoolParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface CoolVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by the {@code Programa}
	 * labeled alternative in {@link CoolParser#prog}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrograma(CoolParser.ProgramaContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Classe}
	 * labeled alternative in {@link CoolParser#class}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClasse(CoolParser.ClasseContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Metodo}
	 * labeled alternative in {@link CoolParser#feature}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMetodo(CoolParser.MetodoContext ctx);
	/**
	 * Visit a parse tree produced by the {@code DeclaracaoFeature}
	 * labeled alternative in {@link CoolParser#feature}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaracaoFeature(CoolParser.DeclaracaoFeatureContext ctx);
	/**
	 * Visit a parse tree produced by the {@code DeclaracaoFormal}
	 * labeled alternative in {@link CoolParser#formal}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaracaoFormal(CoolParser.DeclaracaoFormalContext ctx);
	/**
	 * Visit a parse tree produced by the {@code MenorIgual}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMenorIgual(CoolParser.MenorIgualContext ctx);
	/**
	 * Visit a parse tree produced by the {@code VariasExpr}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariasExpr(CoolParser.VariasExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code NegacaoNot}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNegacaoNot(CoolParser.NegacaoNotContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Falso}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFalso(CoolParser.FalsoContext ctx);
	/**
	 * Visit a parse tree produced by the {@code String}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitString(CoolParser.StringContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Subtracao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubtracao(CoolParser.SubtracaoContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Divisao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDivisao(CoolParser.DivisaoContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Case}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCase(CoolParser.CaseContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Verdadeiro}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVerdadeiro(CoolParser.VerdadeiroContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Adicao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAdicao(CoolParser.AdicaoContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Igual}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIgual(CoolParser.IgualContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprChaves}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprChaves(CoolParser.ExprChavesContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Negacao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNegacao(CoolParser.NegacaoContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Atribuicao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtribuicao(CoolParser.AtribuicaoContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ENulo}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitENulo(CoolParser.ENuloContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Inteiro}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInteiro(CoolParser.InteiroContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Loop}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLoop(CoolParser.LoopContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Multiplicacao}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultiplicacao(CoolParser.MultiplicacaoContext ctx);
	/**
	 * Visit a parse tree produced by the {@code NovoTipo}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNovoTipo(CoolParser.NovoTipoContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprArroba}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprArroba(CoolParser.ExprArrobaContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Menor}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMenor(CoolParser.MenorContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Let}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLet(CoolParser.LetContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Identificador}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdentificador(CoolParser.IdentificadorContext ctx);
	/**
	 * Visit a parse tree produced by the {@code If}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIf(CoolParser.IfContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprParenteses}
	 * labeled alternative in {@link CoolParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprParenteses(CoolParser.ExprParentesesContext ctx);
}