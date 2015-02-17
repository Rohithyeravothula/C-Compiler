def ischar(n):
	l=len(n)
	if(l==3):
		try:
			n=n[1]
			ord(n)
			return 1
		except:
			return 0
	else:
		return 0;


def ishex(n):
	l=len(n)
	oct_l=['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e']
	try:
		if int(n[0])!=0 or n[1]!='x':
			return 0
		else:
			s=n[2:l]
			l=len(s)
			for i in range(0,l):
				if s[i] not in oct_l:
					return 0
		return 1
	except:
		return 0

def isstr(n):
	#print "string",n
	l=len(n)
	try:
		if(n[0]=='"' and n[l-1]=='"'):
			return 1
		else:
			return 0
	except:
		return 0

def isnum(n):
	try:
		p=int(n)
		return 1
	except:
		return 0
def write(n):
	z=open('results.txt','a')
	if(isnum(n) or ischar(n) or isstr(n) or ishex(n)):
		z.write(n+'\n')
	z.close()

a=[]
f=open('testcase.txt','r')
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
for i in range(0,m):
	l=len(a[i])
	for j in range(0,l-1):
		if a[i][j]=='/' and a[i][j+1]=='/': 
			a[i]=a[i][0:j]
			break


i=0
t_char=[',',' ','\n','+','}','-','*','/',';','&','|',')']
while(i<m):
	if a[i]=='' or a[i]=='\n':
		if i<m-1:
			i=i+1
		else:
			break

	s=a[i]
	l=len(s)
	j=0
	#print a[i]
	while(j<l):
		if(s[j]=='='):    # array 
			if(s[j+1]=='{'):
				j=j+2
				t=j
				while(s[t]!='}'):
					t=t+1
				p=s[j:t]
				for num in p.split():
					write(num)					
			else:
				#print "not array"
				j=j+1
				t=j
				if(s[t]=='-'):
					t=t+1
				if(s[t]=='='):
					t=t+1
					j=j+1
				while(s[t] not in t_char):
					t=t+1
				u=s[j:t]
				write(u)
		if(s[j]=='+' or s[j]=='-' or s[j]=='*' or s[j]=='/' or s[j]=='||' or s[j]=='&&' or s[j]=='|' or s[j]=='&'):
			j=j+1
			t=j
			if(s[t]=='-'):
				t=t+1
			while(s[t] not in t_char):
				t=t+1
			u=s[j:t]
			write(u)
		if(s[j]=='<' or s[j]=='>' or s[j]=='!'):
			j=j+1
			t=j
			if(s[t]=='='):
				t=t+1
				j=j+1
			if(s[t]=='-'):
				t=t+1
			while(s[t] not in t_char):
				t=t+1
			u=s[j:t]
			write(u)
		j=j+1
		#print k
	i=i+1		
f.close()
