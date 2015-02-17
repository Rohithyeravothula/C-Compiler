%{
        #include<stdio.h>
        char ch='a';
 
%}

%union {
                char input;
        }

%token <input> NUM
%type <input> E
%left '+' '-'
%right '*' '/'

%%
S : E {printf("t=%c\n",$1);}
  ;

E : E '+' E {printf("%c=%c+%c\n",ch,$1,$3); $$=ch++;}
  | E '-' E {printf("%c=%c-%c\n",ch,$1,$3); $$=ch++;}
  | E '*' E {printf("%c=%c*%c\n",ch,$1,$3); $$=ch++;}
  | E '/' E {printf("%c=%c/%c\n",ch,$1,$3); $$=ch++;}
  | '(' E ')' {$$=$2;}
  | NUM {$$=$1;}
  ;
%%