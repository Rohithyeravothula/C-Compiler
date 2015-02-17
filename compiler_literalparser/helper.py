f=open("testcase.txt",'r')
i=0
while(i<28340):
	i=i+1
	s=f.readline()
	if len(s)>2:
		g=open("testcase2.txt",'a')
		g.write(s)
		g.close()
f.close()
