str=""
l=len(d)
for j in range(0,l):
	str=str+d[j]
str2=""
l=len(c)
for j in range(i,l):
	str2=str2+c[j]
l=len(q)
str3=""
for j in range(0,l):
	str3=str3+q[j]
print str[0]+str3+str[1:len(str)-1]+"\t"+str2
	