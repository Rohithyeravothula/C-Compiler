def write(n):
	l=len(n)
	z=open('results.txt','a')
	z.write(n+'\n')
	z.close()
a=[]
f=open('test.txt','r')
s=f.read()
l=len(s)
i=0
while(i<l-1):
	i=i+1
	#print s[i]
	if(s[i]=='#'):
		i=i+1
		if(s[i:i+6]=='define'):  # of the form #define mak 100
			while(s[i]!='\n'):
				i=i+1
			j=i
			while(s[j]!=' '):
				j=j-1
			u=s[j+1:i]
			write(u)
		if(s[i:i+7]=="include"):
			while(s[i]!='>'):
				i=i+1
i=0
while(i<l):
	i=i+1
	if(s[i]=='{'):
		break
i=i+2
while(i<l):
	j=i
	while(j<l-1):
		j=j+1
		if(s[j]==';'):
			break
	u=s[i:j+1]
	a.append(u)
	i=j+2
# a contains the code lines without ;
m=len(a)
i=0
while(i<m):
	s=a[i]
	l=len(s)
	j=0
	while(j<l):
		k=j
		while(k<l):	
			if(s[k]=='=' or s[k]=='+' or s[k]=='-' or s[k]=='*' or s[k]=='/' or s[k]==',' or s[k]=='{'):
				break
			k=k+1
		t=k+1
		while(t<l):
			if(s[t]==' ' or s[t]=='+' or s[t]=='-' or s[t]=='*' or s[t]=='/' or s[t]==',' or s[t]==';' or s[t]=='}'):
				break
			t=t+1
			
		u=s[k+1:t]
		#print u
		write(u)
		j=t+1
	i=i+1		
f.close()



#problems at array parsing check at array opening
	
