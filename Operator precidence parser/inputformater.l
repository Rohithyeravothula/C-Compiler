%{
#include <stdio.h>
%}

DIGIT [0-9]
NUMBER {DIGIT}+
REAL {DIGIT}*"."{DIGIT}+
TEXT [a-zA-Z ]+
CHAR \'([a-zA-Z])\'
STRING \"([^\\\"]|\\.)*\"
AOPERATOR "+"|"-"|"*"|"/"|"="
BLOCK_BEGINS "{"
BLOCK_ENDS "}"
UNARY "++"|"--"
LOPERATOR "&"|"|"|"&&"|"~"|"||"|">"|"<"|">="|"<="|"=="
%option noyywrap
%%

{DIGIT} { printf("%s\n", yytext); }
{NUMBER} { printf("%s\n", yytext); }
{REAL} { printf("%s\n", yytext); }
{TEXT}   {printf("%s\n",yytext);}
{CHAR}   {printf("%s\n",yytext);}
{STRING}   {printf("%s\n",yytext);}
{AOPERATOR} { printf("%s\n",yytext); }
{LOPERATOR} { ; }
{BLOCK_BEGINS} { ; }
{BLOCK_ENDS} { ; }
{UNARY} { ; }
%%


int main(int argc, char *argv[]) 
{
yylex();
return 0;
}

