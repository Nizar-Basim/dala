%{
#include <stdio.h>
%}

%%

^[aA].*       { printf("Accepted: %s\n", yytext); }
.*            { printf("Non-Accepted: %s\n", yytext); }

%%

int main() {

    printf("Enter text :\n");


    yylex();

    return 0;
}

int yywrap() {
    return 1;
}
