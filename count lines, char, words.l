%{
#include <stdio.h>

int words = 0;
int characters = 0;
int lines = 0;
int in_word = 0;

void count_word() {
    if (in_word) {
        words++;
        in_word = 0;
    }
}

%}

%%
\n        { lines++; characters++; count_word(); }
[ \t]     { characters++; count_word(); }
.         { characters++; in_word = 1; }
%%

int main() {

    printf("Enter text :\n");


    yylex();


    count_word();


    printf("Number of characters: %d\n", characters);
    printf("Number of words: %d\n", words);
    printf("Number of lines: %d\n", lines);

    return 0;
}

int yywrap() {
    return 1;
}
