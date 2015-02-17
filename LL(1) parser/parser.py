import copy

# function definition part
def remove_duplicates(T):
	t=[]
	l=len(T)
	for i in range(0,l):
		if T[i] not in t:
			t.append(T[i])
	return t
def first(s):
	a=[]
	l=len(h)
	for i in range(0,l):
		if s==h[i]:
			x=g[i]
			#print x
			r=len(x)
			if r==1 and s!=x:
				a=a+[x]
			for v in range(0,r):
				if s==x[v]:
					#print "broke"
					break
			for j in range(0,v):
				#print x[j]
				if x[j] in t:
					#print x[j]
					a=a+[x[j]]
					#print a,x[j]
					break
				else:	
					if x[j]!=s:
						dummy=first_nt[nt.index(x[j])]
						if len(dummy)==0:
							dummy=first(x[j])
						#print x[j],dummy
						if '^' not in dummy:
							a=a+dummy
							return a
						else:
							a=a+dummy
							continue
					else:
						return a
	return remove_duplicates(a)
def refirst():
	l=len(g)
	for i in range(0,l):
		if g[i]=='^':
			print "yes"
			first_val[nt.index(h[i])]=first_val[nt.index(h[i])]+['^']
			print first_val[nt.index(h[i])]


def follow(s):
	a=[]
	if s==nt[0]:
		a=a+['$']
	l=len(g)
	for i in range(0,l):
		x=g[i]
		#print x
		r=len(x)
		for j in range(0,r-1):
			if s==x[j]:
				y=x[j+1]
				if y in t:
					a=a+[y]
					break
				else:
					if y==nt[0]:
						dummy=['$']+first_val[nt.index(y)]
						if '^' not in dummy:
							a=a+dummy
						else:
							del dummy[dummy.index('^')]
							a=a+dummy
							break
					else:
						dummy=first_val[nt.index(y)]
						#print y,dummy
						if '^' not in dummy:
							a=a+dummy
						else:
							del dummy[dummy.index('^')]
							a=a+dummy
							break
	return remove_duplicates(a)

def secondfollow():
	r=len(g)
	for i in range(0,r):
		s=g[i]
		l=len(s)
		if s[l-1] not in t and '^' not in first_val[nt.index(s[l-1])]:
			dummy_follow[nt.index(s[l-1])]=dummy_follow[nt.index(s[l-1])]+dummy_follow[nt.index(h[i])]
def thirdfollow():
	null_handles=[]
	l=len(g)
	for i in range(0,l):
		if g[i]=='^':
			null_handles.append(h[i])
	for i in range(0,l):
		s=g[i]
		r=len(s)
		if s[r-1] in null_handles:
			#print "adding ",s[r-1],h[i]
			dummy_follow[nt.index(s[r-2])]=dummy_follow[nt.index(s[r-2])]+dummy_follow[nt.index(h[i])]

# function definiton part end

#grammer formatting
f=open("grammer.txt","r")
d1=[]
d2=[]
while True:
	x=f.readline()
	if x=="EOF":
		break
	l=len(x)
	for i in range(0,l-1):
		if x[i:i+2]=="->":
			break
	d1.append(x[0:i])
	d2.append(x[i+2:l-1])
f.close()
h=[]
g=[]
l=len(d2)
for i in range(0,l):
	s=d2[i]
	d=[]
	d=s.split('|')
	r=len(d)
	for j in range(0,r):
		h.append(d1[i])
		g.append(d[j])
#g contains grammer and h contains handles
l=len(g)
T=[]
for i in range(0,l):
	s=g[i]
	#print s
	r=len(s)
	for j in range(0,r):
		if ord(s[j]) not in range(65,91):
			T.append(s[j])

t=[]
t=remove_duplicates(T)
nt=remove_duplicates(h)

# t contains terminals and nt contains non-terminals

first_t=[]
l=len(t)
for i in range(0,l):
	first_t.append([t[i]])
l=len(nt)
# finding first of non terminals
# first parsing
first_nt=[]
l=len(nt)
for i in range(0,l):
	first_nt.append([])
for i in range(0,l):
	x=nt[i]
	r=len(h)
	for j in range(0,r):
		if x==h[j]:
			s=g[j]
			if g[j][0] in t:
				first_nt[i].append(g[j][0])

# first parsing done
l=len(nt)
first_val=[]
for i in range(0,l):
	first_val.append(first(nt[i]))

f=open("first.txt",'w')
for i in range(0,l):
	x=first_val[i]
	r=len(x)
	s=""
	for j in range(0,r):
		s=s+x[j]
	f.write(s+"\n")
f.write("EOF")
f.close()
# first_t contains list of firts of termibnals
#first_val contains list of first of non-terminals

l=len(nt)
dummy_follow=[]
for i in range(0,l):
	dummy_follow.append(follow(nt[i]))
count =10
secondfollow()
thirdfollow()
secondfollow()
l=len(dummy_follow)
for i in range(0,l):
	dummy_follow[i]=remove_duplicates(dummy_follow[i])
follow_val=dummy_follow
first_val=[]
f=open("first.txt",'r')
while True:
	s=f.readline()
	if s=="EOF":
		break
	l=len(s)
	dummy=[]
	for i in range(0,l-1):
		dummy.append(s[i])
	first_val.append(dummy)


# first_val contains values of first and follow_val contains follow values

# table construction 


table=[]
l=len(nt)
for i in range(0,l):
	dummy=[]
	r=len(t)+1
	for j in range(0,r):
		dummy.append([])
	table.append(dummy)
l=len(g)
first_pdn=[]
for i in range(0,l):
	first_pdn.append([])
for i in range(0,l):
	s=g[i]
	if s[0] in t:
		first_pdn[i]=[s[0]]
	else:
		first_pdn[i]=first_val[nt.index(s[0])]
		if '^' in first_val[nt.index(s[0])]:
			j=0
			while s[j] not in t and '^' not in first_val[nt.index(s[j])]:
				first_pdn[i]=first_pdn[i]+first_val[nt.index(s[j])]
				j=j+1
		
l=len(h)
t.append('$')
for i in range(0,l):
	dummy=first_pdn[i]
	r=len(dummy)
	for j in range(0,r):
		u=nt.index(h[i])
		v=t.index(dummy[j])
		s=h[i]+"->"+g[i]
		table[u][v].append(s)
	if '^' in dummy:
		dummy=follow_val[nt.index(h[i])]
		r=len(dummy)
		for j in range(0,r):
			u=nt.index(h[i])
			v=t.index(dummy[j])
			s=h[i]+"->"+"^"
			table[u][v].append(s)

l=len(nt)
u=t.index('^')
del t[u]
for i in range(0,l):
	del table[i][u]
print t
for i in range(0,l):
	print nt[i],table[i]
for i in range(0,l):
	for j in range(0,len(t)):
		if len(table[i][j])>1:
			print "error in grammer"
#table ready
# t terminal does not contain '^'





while True:
	print "enter input"
	x=raw_input()
	if x=="break" or x=="BREAK":
		print "END"
		break
	l=len(x)
	input_stack=[]   #start symbol
	for i in range(0,l):
		input_stack.append(x[i])
	output_stack=['$',nt[0]]   #
	input_stack.append('$')
	l=len(input_stack)
	i=0
	while(i<l):
		z=len(output_stack)
		if input_stack[i] not in t and input_stack[i] not in nt:
			print "error grammar symbol ",input_stack[i]
			break
		if output_stack[z-1]=='^':
			output_stack.pop()
			continue
		if output_stack[z-1] not in t:
			u=nt.index(output_stack[z-1])
			v=t.index(input_stack[i])
			print u,v,output_stack[z-1],input_stack[i]
			del output_stack[z-1]
			s=table[u][v][0]
			print s
			y=len(s)
			for e in range(0,y-1):
				if s[e:e+2]=="->":
					break
			e=e+2
			dummy=[]
			for u in range(e,y):
				dummy.append(s[u])
			dummy.reverse()
			print "dummy",dummy
			output_stack=output_stack+dummy

		else:
			if output_stack[z-1]==input_stack[i]:
				output_stack.pop()
				i=i+1		
			else:
				print "error"
				break
		print input_stack[i:l],output_stack
