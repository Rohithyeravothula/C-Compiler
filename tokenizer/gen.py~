import random
a=[]
f=open("program.c",'r')
s=f.read()
a=s.split(';')
f.close()
f=open("roh.txt","a")
l=len(a)
i=8000
while(i>0):
	i=i-1
	r=random.random()*(l-1)
	f.write(a[int(r)]+';')
f.close()

