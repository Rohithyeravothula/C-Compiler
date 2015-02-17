
def chnum(n):
	try:
		p=int(n)
		return 1
	except:
		return 0
def write(n):
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

for i in range(0,m):
	a[i]=a[i].replace(" ","")
	print a[i]
i=0
t_char=[',',' ','\n','+','}','-','*','/',';']
while(i<m):
	s=a[i]
	l=len(s)
	j=0
	print a[i]
	while(j<l):
		k=j
		while(k<l):	
			if(s[k]=='='):
				if(s[k+1]=='{'):
					k=k+2
					t=k+1
					while(s[t] not in t_char):
						t=t+1
					u=s[k:t]
					print u
					write(u)
					k=t
				else:
					t=k+1
					while(s[t] not in t_char):
						t=t+1
					u=s[k:t]
					write(u)
					k=t
			if(s[k]=='+' or s[k]=='-' or s[k]=='*' or s[k]=='/'):
				t=k+1
				while(s[t] not in t_char):
					t=t+1
				u=s[k:t]
				write(u)
				k=t
			k=k+1
			print k
	i=i+1		
f.close()



#problems at array parsing check at array opening
	