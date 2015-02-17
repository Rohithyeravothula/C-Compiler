%{
#include <stdio.h>
%}

DIGIT [0-9]
NUMBER {DIGIT}+
REAL {DIGIT}*"."{DIGIT}+
TEXT [a-zA-Z ]+
TEXT_NUMBERS [a-zA-Z0-9]
CONDITIONALS "if"|"else"|"else if"|"switch"|"case"
KEYWORD "main"|"break"|"continue"|"goto"|"printf"|"scanf"|"sprintf"|"sscanf"|"fopen"|"fwrite"|"fread"|"fclose"|"write"|"read"|"open"|"close"|"return"|"int"|"float"|"char"|"unsigned"|"signed"|"short"|"long"|"double"
ITERATORS "for"|"while"|"do"
PREPROCESSOR "#"|"#line"|"#undef"|"#error"|"#elif"|"#else"|"#endif"|"#if"|"#define"|"#include"|"#pragma"|"#ifndef"|"#ifdef"
DELIMITER [; :\t\n()"]
CHAR \'([a-zA-Z])\'
STRING \"([^\\\"]|\\.)*\"
IDENTIFIER [a-zA-Z]{TEXT_NUMBERS}*|[a-zA-Z]{TEXT_NUMBERS}*[[{NUMBER}+]]
NON_IDENTIFIER {NUMBER}+[A-Za-z]+
FORMAT_SPECIFIER "%"{TEXT_NUMBERS}+
FILE "<"{IDENTIFIER}.h">"
COMMENT "/*"[a-zA-Z0-9 \t\n;.~!@#$%^&*()_+=<>?:"{}]*"*/"
AOPERATOR "+"|"-"|"*"|"/"|"="
BLOCK_BEGINS "{"
BLOCK_ENDS "}"
UNARY "++"|"--"
LOPERATOR "&"|"|"|"&&"|"~"|"||"|">"|"<"|">="|"<="|"=="
FUNCTION {IDENTIFIER}+"("{DELIMITER}*{TEXT}{TEXT_NUMBERS}*{DELIMITER}*")"
%option noyywrap
%%

{CONDITIONALS} { ; }
{ITERATORS} { ; }
{DIGIT} { printf("%s\n", yytext); }
{NUMBER} { printf("%s\n", yytext); }
{REAL} { printf("%s\n", yytext); }
{PREPROCESSOR} { ; }
{DELIMITER} {; }
{CHAR}   {printf("%s\n",yytext);}
{STRING}   {printf("%s\n",yytext);}
{KEYWORD} { ; }
{NON_IDENTIFIER} {; }
{IDENTIFIER} { printf("%s\n", yytext); }
{COMMENT} {; }
{AOPERATOR} { ; }
{LOPERATOR} { ; }
{BLOCK_BEGINS} { ; }
{BLOCK_ENDS} { ; }
{FILE} { ; }
{UNARY} { ; }
{FUNCTION} { ; }
{FORMAT_SPECIFIER} {; }
%%


int main(int argc, char *argv[]) 
{
yylex();
return 0;
}


