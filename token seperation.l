%{
#include <stdio.h>
%}

%%

[0-9]+\.[0-9]+                printf("%s is a floating point number\n", yytext);
int|float|char|double|void    printf("%s is a datatype\n", yytext);
[0-9]+                        printf("%s is an integer number\n", yytext);
[a-zA-Z_][a-zA-Z0-9_]*\(\)     printf("%s is a function\n", yytext);
[a-zA-Z_][a-zA-Z0-9_]*        printf("%s is an identifier\n", yytext);
[+=*/-]                       printf("%s is an operator\n", yytext);
;                             printf("%s is a delimiter\n", yytext);
,                             printf("%s is a separator\n", yytext);
#[a-zA-Z_\.]+                 printf("%s is a preprocessor\n", yytext);
[ \t\n]                        ;
.                             printf("%s is an unknown token\n", yytext);

%%

int yywrap(void) {
    return 1;
}

int main() {
    printf("Enter text :\n");
    yylex();
    return 0;
}
