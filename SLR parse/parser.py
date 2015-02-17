def remdup(a):
	l=len(a)
	b=[]
	for i in range(0,l):
		if a[i] not in b:
			b.append(a[i])
	return b



f=open("grammar.txt","r")
h=[]
while True:
	s=f.readline()
	if s=="EOF":
		break
	h.append(s[0:len(s)-1])
l=len(h)
L=[]
R=[]
for i in range(0,l):
	s=h[i]
	r=len(s)
	for j in range(1,r-1):
		if s[j:j+2]=="->":
			break
	L.append(s[0:j])
	R.append(s[j+2:r])
l=len(L)
terminal=[]
for i in range(0,l):
	s=R[i]
	r=len(s)
	for j in range(0,r):
		if ord(s[j])<65 or ord(s[j])>90:
			terminal.append(s[j])

nonterminal=[]
for i in range(0,l):
	if L[i] not in terminal and L[i] not in nonterminal:
		nonterminal.append(L[i])

#code to find first and follow
first_nontermial=[]
l=len(nonterminal)
for i in range(0,l):
	first_nontermial.append([])

l=len(L)
for i in range(0,l):
	s=R[i]
	p=L[i]
	j=0
	r=len(s)
	while j<r:
		if s[j] in terminal:
			first_nontermial[nonterminal.index(p)]=first_nontermial[nonterminal.index(p)]+[s[j]]
			break
		break
count=0
while count<5:
	for i in range(0,l):
		s=R[i]
		p=L[i]
		r=len(s)
		j=0
		while j<r:
			if s[j] in terminal:
				break
			g=first_nontermial[nonterminal.index(s[j])]
			if '^' not in g:
				first_nontermial[nonterminal.index(p)]=first_nontermial[nonterminal.index(p)]+g
				break
			else:
				first_nontermial[nonterminal.index(p)]=first_nontermial[nonterminal.index(p)]+g
				j=j+1
	count=count+1
l=len(first_nontermial)
for i in range(0,l):
	first_nontermial[i]=remdup(first_nontermial[i])

# first done

# code to find follow 
follow_nonterminal=[]
l=len(nonterminal)
for i in range(0,l):
	follow_nonterminal.append([])
follow_nonterminal[0]=['$']
l=len(R)
for i in range(0,l):
	s=R[i]
	r=len(s)
	j=1
	while j<r:
		if s[j] in terminal and s[j-1] not in terminal:
			follow_nonterminal[nonterminal.index(s[j-1])]=follow_nonterminal[nonterminal.index(s[j-1])]+[s[j]]
		j=j+1
for i in range(0,l):
	s=R[i]
	r=len(s)
	j=0
	while j<r-1:
		if s[j] in nonterminal and s[j+1] in nonterminal:
			g=first_nontermial(nonterminal.index(s[j+1]))
			if '^' not in g:
				follow_nonterminal[nonterminal.index(s[j])]=follow_nonterminal[nonterminal.index(s[j])]+g
				break
			else:
				del g[g.index('^')]
				follow_nonterminal[nonterminal.index(s[j])]=follow_nonterminal[nonterminal.index(s[j])]+g
		j=j+1
for i in range(0,l):
	s=R[i]
	p=L[i]
	r=len(s)
	j=r-1
	if s[j] in nonterminal:
		follow_nonterminal[nonterminal.index(s[j])]=follow_nonterminal[nonterminal.index(s[j])]+follow_nonterminal[nonterminal.index(p)]	
	while j>=0:
		if s[j] in nonterminal and '^' in first_nontermial[nonterminal.index(s[j])]:
			j=j-1
		break
	if j!=r-1:
		j=j+1
		follow_nonterminal[nonterminal.index(s[j])]=follow_nonterminal[nonterminal.index(s[j])]+follow_nonterminal[nonterminal.index(p)]

l=len(follow_nonterminal)
for i in range(0,l):
	follow_nonterminal[i]=remdup(follow_nonterminal[i])



# follow done
def printlist(a):
	l=len(a)
	for i in range(0,l):
		print a[i]
def getclosure(a):  # return list of tuple , each tuplr contains single production as [L[i],R[i]]
	l=len(L)
	closurelist=[]
	for i in range(0,l):
		if L[i]==a:
			closurelist.append([L[i],R[i]])
	closurelist=remdup(closurelist)
	p1=len(closurelist)
	while True:
		l=len(closurelist)
		for i in range(0,l):
			r=len(L)
			for j in range(0,r):
				if L[j]==closurelist[i][1] and [L[j],R[j]] not in closurelist:
					closurelist.append([L[j],R[j]])
		closurelist=remdup(closurelist)
		p2=len(closurelist)
		if p2==p1:
			break
		p1=p2
	return closurelist

#print nonterminal[0],getclosure(nonterminal[0])

def generatestates(statelist,position): # returns statelist on basis of position of dot and nonterminals
	l=len(statelist)
	list_nonterminals=[]
	for i in range(0,l):
		if position < len(statelist[i]) and statelist[i] in nonterminal:
			list_nonterminals.append(statelist[i])
	l=len(list_nonterminals)
	closurelist=[]
	for i in range(0,l):
		closurelist.append(getclosure(list_nonterminals[i]))
	closurelist=remdup(closurelist)
	#print closurelist[0]
	l=len(closurelist[0])
	for i in range(0,l):
		closurelist[0][i]=[closurelist[0][i],position]
	return closurelist[0] # remember it returns a complex list 

# print generatestates([nonterminal[0]],0)


finalstates=[]
#print generatestates(nonterminal[0],0)
finalstates.append(generatestates(nonterminal[0],0)) # state 0 need to construct remaning states
l=len(R)
for i in range(0,l):
	r=len(R[i])
	for j in range(0,r):
		h=[[[L[i],R[i]],j+1]]
		if j<r-1 and R[1+j] in nonterminal:
			E=getclosure(R[1+j])
			k=len(E)
			for u in range(0,k):
				h.append([E[u],0])  # generate closure so . at first position
		finalstates.append(h)


# modifying finalstates accordingly
dummy=finalstates[2]
finalstates[1]=finalstates[1]+finalstates[2]
del finalstates[2]
dummy=finalstates[4]
finalstates[4]=finalstates[4]+finalstates[5]
del finalstates[5]
del finalstates[5][2],finalstates[5][1]
finalstates[9].append([[L[1],R[1]],0])
finalstates[9].append([[L[2],R[2]],0])
finalstates[9][4],finalstates[9][6]=finalstates[9][6],finalstates[9][4]
finalstates[9][3],finalstates[9][5]=finalstates[9][5],finalstates[9][3]
finalstates[9][2],finalstates[9][3]=finalstates[9][3],finalstates[9][2]
finalstates[9][1],finalstates[9][4]=finalstates[9][4],finalstates[9][1]
finalstates[10].append([[L[1],R[1]],1])
finalstates[9],finalstates[8]=finalstates[8],finalstates[9]
finalstates[8][0][1]=1
finalstates[9][0][1]=2
finalstates[3]=finalstates[3]+[[L[3],R[3]],1]
finalstates[9]=finalstates[9]+finalstates[10][1]
del finalstates[10][1]
finalstates[9]=[finalstates[9][0],[finalstates[9][1],finalstates[9][2]]]
finalstates[3]=[finalstates[3][0],[finalstates[3][1],finalstates[3][2]]]

def getgototable(i,j,k):
	i=0
	j=2
	k=7
	gototable[i][j]=k
	i=i+2
	gototable[i][j]=k
	i=i+6
	gototable[i][j]=k
	i=j=k=0
	k=k+1
	gototable[i][j]=k
	j=j+1
	gototable[i][j]=k+3
	gototable[i+2][j]=k+2
	i=i+5
	k=6
	gototable[i][j+1]=k
	i=j=0
	j=j+8
	for i in range(0,2):
		gototable[j][i]=k
	gototable[j][i]=gototable[j][i]-4
# modification done
#printlist(finalstates)
#print finalstates[9]

gototable=[]
l=len(nonterminal)
r=len(finalstates)
for i in range(0,r):
	dummy=[]
	for j in range(1,l):
		dummy.append("E")
	gototable.append(dummy)

getgototable(i,j,k)
#printlist(gototable)
#print nonterminal
# develop reduce lists start

reducelist=[]
l=len(finalstates)
for i in range(1,l):  # no need to check I0 state for reductions
	r=len(finalstates[i])
	for j in range(0,r):
		position=finalstates[i][j][1]
		pdn=finalstates[i][j][0][1]
		if len(pdn)==position:
			reducelist.append([i,finalstates[i][j][0]])
del reducelist[0]  # delete augmented grammer symbol's frst symbol pdn
#printlist(reducelist)
# reduce list done 

# shift list building start
headproduction=[] # contains head pdn in every state required for finding shift actions
l=len(finalstates)
for i in range(0,l):
	headproduction.append(finalstates[i][0])
#printlist(headproduction)

shiftlist=[]
for i in range(0,l):
	r=len(finalstates[i])
	for j in range(0,r):
		position=finalstates[i][j][1]
		pdn=finalstates[i][j][0][1]
		if position<len(pdn) and pdn[position] in terminal:
			newpdn=[finalstates[i][j][0],finalstates[i][j][1]+1]
			index=headproduction.index(newpdn)
			shiftlist.append([pdn[position],i,index])
#printlist(shiftlist)
# shift list done


actiontable=[]
terminal.append("$")
length_terminals=len(terminal)
length_nonterminals=len(nonterminal)
length_states=len(finalstates)

for i in range(0,length_states):
	dummy=[]
	for j in range(0,length_terminals):
		dummy.append("E")
	actiontable.append(dummy)
l=len(shiftlist)
for i in range(0,l):
	index=terminal.index(shiftlist[i][0])
	actiontable[shiftlist[i][1]][index]="S"+str(shiftlist[i][2])

l=len(reducelist)
for i in range(0,l):
	index=nonterminal.index(reducelist[i][1][0])
	dummy=follow_nonterminal[index]
	r=len(dummy)
	index_pdn=R.index(reducelist[i][1][1])
	for j  in range(0,r):
		index=terminal.index(dummy[j])
		actiontable[reducelist[i][0]][index]=str("R")+str(index_pdn)

actiontable[1][terminal.index("$")]="Accepted"
#printlist(actiontable)
#printlist(reducelist)
#print follow_nonterminal

# parsing inpt section



# infomation
print "Grammer"
l=len(L)
for i in range(0,l):
	print L[i]+" "+"->"+" "+R[i]
print "Terminal:"
print terminal
print "Nonterminal:"
print nonterminal
print "First of nonterminal"
print first_nontermial
print "Follow of nonterminal:"
print follow_nonterminal
print "States:"
printlist(finalstates)
print "Action table"
printlist(actiontable)
print "Gototable:"
printlist(gototable)

print "Parsing input starts:"
for i in range(0,8):
	print 
# end information
f=open("input.txt",'r')
while True:
	l=f.readline()
	if l=="EOF":
		break
	x=l[0:len(l)-1]
#print x
# x contains the input
inputstack=[]
parserstack=[]
l=len(x)
for i in range(0,l):
	inputstack.append(x[i])
	#print x[i]
inputstack.append("$")
#print inputstack
parserstack.append("0")
i=0
j=0
#printlist(actiontable)
# main parsing of input
while True:
	print "Inputstack:"
	print inputstack
	print "Parser stack:"
	print parserstack
	count=count-1
	index_parser=int(parserstack[j])
	if inputstack[i] in nonterminal:
		index_input=nonterminal.index(inputstack[i])-1
	elif inputstack[i] in terminal:
		index_input=terminal.index(inputstack[i])
	action=actiontable[index_parser][index_input]
	print index_parser,index_input
	if action[0]=="S":
		dummy=inputstack[i]
		parserstack.append(dummy)
		parserstack.append(action[1:len(action)])
		del inputstack[i]
		j=j+2
		print "Action Shift as "+" "+action
	elif action[0]=="R":
		index_pdn=action[1:len(action)]
		pdn_rule=R[int(index_pdn)]
		pdn_left=L[int(index_pdn)]
		l=len(pdn_rule)
		parserstack=parserstack[0:j+1-2*l]
		j=j-2*l
		#print parserstack,j
		index=int(parserstack[j])
		parserstack.append(pdn_left)
		index_nonterminal=nonterminal.index(pdn_left)-1
		#print index,index_nonterminal
		nextnum=gototable[index][index_nonterminal]
		parserstack.append(str(nextnum))
		j=j+2
		print "Action Reduce as"+" "+action+" "+"production rule"+" "+pdn_left+"->"+pdn_rule
	elif action=="Accepted":
		print "Accepted"
		break

























