# returns list of terminal and non terminal at a particular position
def numberout(a,n):
	l=len(a)
	t=[]
	nt=[]
	for i in range(0,l):
		try:
			if a[i][1][n] in nonterminal:
				nt.append(a[i][1][n])
			else:
				t.append(a[i][1][n])
		except:
			continue
	t=remdup(t)
	nt=remdup(nt)
	return [t,nt]

# returns closure of the given set remember does not return as L and R returns a production as [lhs,rhs]
def getclosur(a):
	l=len(a)
	cl=[]
	for i in range(0,l):
		index=nonterminal.index(a[i])
		cl.append([L[index],R[index]])
	l=len(cl)
	for i in range(0,l):
		cl[i]=remdup(cl[i])
	return cl





#closure=[[]]
#l=len(L)
#for i in range(0,l):
#	closure[0].append([L[i],R[i]])
#pos=0
#while True:
#	t,nt=numberout(closure[pos],pos)
#	break


def getclosure(a):
	
listofstates=[[]]
while True:
	l=len(L)
	for i in range(0,l):
		if R[i] in nonterminal:
			listofstates[0].append(getclosur())








futurelist=[] # list of nonterminals with . position
l=len(finalstates[0])
for i in range(0,l):
	if finalstates[0][i][1]<len(finalstates[0][i][0][1]):
		futurelist.append([finalstates[0][i][0][1][finalstates[0][i][1]],finalstates[0][i][1]])
futurelist=remdup(futurelist)
print futurelist
#print finalstates

reducelist=[]
l=len(finalstates)
for i in range(1,l):  # no need to check I0 state for reductions
	r=len(finalstates[i])
	for j in range(0,r):
		position=finalstates[i][j][1]
		pdn=finalstates[i][j][0][1]
		if len(pdn)==position:
			reducelist.append([finalstates[i][j][0][0],])

#gototable[i][j+1]=6
#gototable[0][0]="1"
#gototable[0][1]="4"
#gototable[0][2]="7"
#gototable[2][1]="3"
#gototable[2][2]="7"
#gototable[5][2]="6"
#gototable[8][0]="9"
#gototable[8][1]="5"
#gototable[8][2]="7"
