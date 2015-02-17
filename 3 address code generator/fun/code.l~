%{
        #include<stdio.h>
        #include"y.tab.h"
        
%}
%%
[0-9A-Z]+      {yylval.input=yytext[0]; return NUM;}
\n          {return 0;}
.           {return yytext[0];}
%%
void yyerror(char* s)
{
        printf("%s\n",s);
}
main()
{
        yyparse();
        return 0;
}
