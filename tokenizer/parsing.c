#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
int ch(char *a,int l)
{
    int i;
    for(i=0;i<l;i++)
    if(a[i]!='.' && isdigit(a[i])==0)
    return 0;
    return 1;
}
main()
{
FILE *fp;
fp=fopen("output.txt","rt");
char buf[40];
char a[1000][20];
int f[1000],i,j,l;
for(j=0;j<1000;j++)
f[j]=-1;
i=0;
while(fgets(buf,1000,fp)!=NULL)
{
	char s[40];
	memset(s,'\0',sizeof(s));
	if(buf[0]==',' || buf[0]=='[')
	{strcpy(s,buf+1);
	l=strlen(s);
	s[l-1]='\0';
	}
	else
	{strcpy(s,buf);
	l=strlen(s);
	s[l-1]='\0';}
	for(j=0;j<i;j++)
	if(strcmp(s,a[j])==0)
	{
		f[j]++;
		break;
	}
	if(j==i)
	{
	strcpy(a[i],s);
	i++;
	f[i]=1;
	}
}
for(i=0;i<1000;i++)
if(f[i]!=-1)
	{
	l=strlen(a[i]);
	if(ch(a[i],l)==0)
	{
	if(a[i][0]=='"' || a[i][0]=='\'')
	printf("literal: %s\n",a[i]);	
	else
	printf("Identifier: %s frequency: %d\n",a[i],f[i]);
	}
	else
	{
		l=strlen(a[i]);
		for(j=0;j<l;j++)
		if(a[i][j]=='.')
			break;	
		if(j==l)
			printf("literal: %d\n",atoi(a[i]));
		else
			printf("literal: %f\n",atof(a[i]));
	}
	}
return 0;
}


