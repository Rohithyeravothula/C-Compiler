
%{
        #include<stdio.h>
 
%}

%union {
                char dval;
        }

%token <dval> NUM
%type <dval> E
%left '+' '-'
%right '*' '/'

%%
S : E {printf("\nt = %c\n",$1);}
  ;

E : E '+' E {$$=fun($$,$1,'+',$3);}
  | E '-' E {$$=fun($$,$1,'-',$3);}
  | E '*' E {$$=fun($$,$1,'*',$3);}
  | E '/' E {$$=fun($$,$1,'/',$3);}
  | '(' E ')' {$$=$2;}
  | NUM {$$=$1;}
  ;
%%