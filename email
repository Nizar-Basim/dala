%{
#include<stdio.h>
%}

%%

^[a-z][a-z0-9_]*(@[A-Za-z]+)(\.[a-z]+)+ {printf("valid\n");}
.* {printf("invalid\n");}

%%

int main()
{
    printf("Enter email: ");
    yylex();
    return 0;
}
