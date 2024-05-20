%{
#include <stdio.h>

int vowels = 0;
int consonants = 0;

%}

%%
[aeiouAEIOU]     { vowels++; }
[a-zA-Z] { consonants++; }
.                {  }
\n               {  }
%%

int main() {

    printf("Enter a string :\n");

    yylex();

    printf("Number of vowels: %d\n", vowels);
    printf("Number of consonants: %d\n", consonants);

    return 0;
}

int yywrap() {
    return 1;
}
