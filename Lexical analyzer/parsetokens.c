#include<stdio.h>
#include<string.h>
main()
{
	FILE *f;
	f=open('test.txt','a');
	char a;
	while((a=getchar()!=NULL))
		putchar(a);
	return 0;
}
