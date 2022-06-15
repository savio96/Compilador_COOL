grammar Cool;
prog    :   (class ';')+ EOF #Programa
        ;
class   :   'class' TYPE ('inherits' TYPE)? '{' (feature ';')* '}' #Classe
        ;
feature :   ID'('(formal (','formal)*)?')' ':' TYPE '{' expr '}' #Metodo
        |   ID ':' TYPE ('<-' expr)? #DeclaracaoFeature
        ;
formal  :   ID ':' TYPE #DeclaracaoFormal
        ;
expr    :   ID '<-' expr #Atribuicao
        |   expr ('@'TYPE)?'.'ID'('(expr (','expr)*)?')' #ExprArroba
        |   ID '('(expr (',' expr)*)?')' #VariasExpr
        |   'if' expr 'then' expr 'else' expr 'fi' #If
        |   'while' expr 'loop' expr 'pool' #Loop
        |   '{'(expr ';')+'}' #ExprChaves
        |   'let' ID ':' TYPE ('<-' expr)? (',' ID ':' TYPE ('<-' expr)?)* 'in' expr #Let
        |   'case' expr 'of' (ID ':' TYPE '=>' expr ';')+ 'esac' #Case
        |   'new' TYPE     #NovoTipo
        |   'isvoid' expr  #ENulo
        |   expr '+' expr  #Adicao
        |   expr '-' expr  #Subtracao
        |   expr '*' expr  #Multiplicacao
        |   expr '/' expr  #Divisao
        |   '~'expr        #Negacao
        |   expr '<' expr  #Menor
        |   expr '<=' expr #MenorIgual
        |   expr '=' expr  #Igual
        |   'not' expr     #NegacaoNot
        |   '('expr')'     #ExprParenteses
        |   ID             #Identificador
        |   INTEGER        #Inteiro
        |   STRING         #String
        |   'true'         #Verdadeiro
        |   'false'        #Falso
        ;

ID           :   ('a'..'z')('a'..'z'|'A'..'Z'|'_'|'0'..'9')*;
TYPE         :   ('A'..'Z')('a'..'z'|'A'..'Z'|'_'|'0'..'9')*;
STRING       :   '"' ( ESC | . )*? '"';
INTEGER      :   [0-9]+ ;

WS           :   [ \b\t\n\f]+   -> channel(HIDDEN);
LINE_COMMENT :   '--' .*? '\n' -> channel(HIDDEN);
COMMENT      :   '(*' .*? '*)' -> channel(HIDDEN);

fragment ESC : '\\' [btnr"\\] ; //
