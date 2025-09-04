grammar Fibo;

prog : 'FIBO' '(' INT ')' ;
INT  : [0-9]+ ;
WS   : [ \t\r\n]+ -> skip ;
