a=[]
f=open('testgenerator.txt','r')
s=f.read()
l=len(s)
i=0
r=""
while(i<l-1):
	if s[i]=='/' and s[i+1]=='*':
		while(s[i]!='*' or s[i+1]!='/'):
			i=i+1
		i=i+1
	else:
		r=r+s[i]
		i=i+1
s=r
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
			#write(u)
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
for i in range(0,m):
	l=len(a[i])
	for j in range(0,l-1):
		if a[i][j]=='/' and a[i][j+1]=='/': 
			a[i]=a[i][0:j]
			break
import random
m=len(a)
for i in range(0,15000):
	j=random.randint(0,m-1)
	f=open("testcase.txt",'a')
	f.write(a[j]+'\n')
	f.close()