grammar Cool;
prog    :   (class ';')+ ;
class   :   'class' TYPE ('inherits' TYPE)? '{' (feature ';')* '}';
feature :   ID'('(formal (','formal)*)?')' ':' TYPE '{' expr '}'
        |   ID ':' TYPE ('<-' expr)?
        ;
formal  :   ID ':' TYPE ;
expr    :   ID '<-' expr
        |   expr ('@'TYPE)?'.'ID'('(expr (','expr)*)?')'
        |   ID '('(expr (',' expr)*)?')'
        |   'if' expr 'then' expr 'else' expr 'fi'
        |   'while' expr 'loop' expr 'pool'
        |   '{'(expr ';')+'}'
        |   'let' ID ':' TYPE ('<-' expr)? (',' ID ':' TYPE ('<-' expr)?)* 'in' expr
        |   'case' expr 'of' (ID ':' TYPE '=>' expr)+ 'esac'
        |   'new' TYPE
        |   'isvoid' expr
        |   expr '+' expr
        |   expr '-' expr
        |   expr '*' expr
        |   expr '/' expr
        |   '~'expr
        |   expr '<' expr
        |   expr '<=' expr
        |   expr '=' expr
        |   'not' expr
        |   '('expr')'
        |   ID
        |   INTEGER
        |   STRING
        |   'true'
        |   'false'
        ;

ID           :   ('a'..'z')('a'..'z'|'A'..'Z'|'_'|'0'..'9')*;
TYPE         :   ('A'..'Z')('a'..'z'|'A'..'Z'|'_'|'0'..'9')*;
STRING       :   '"' ( ESC | . )*? '"';
INTEGER      :   [0-9]+ ;

WS           :   [ \r\b\t\n\f]+   -> channel(HIDDEN);
LINE_COMMENT :   '--' .*? '\n' -> channel(HIDDEN);
COMMENT      :   '(*' .*? '*)' -> channel(HIDDEN);

fragment ESC : '\\' [btnr"\\] ; //
