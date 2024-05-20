%{
#include <stdio.h>
%}

%%

[0-9]+ {
    int num = atoi(yytext);
    if(num % 2 == 0)
        printf("%d is even\n", num);
    else
        printf("%d is odd\n", num);
}

%%

int yywrap() {
    return 1;
}

int main() {
    printf("enter any number: ");
    yylex();
    return 0;
}
