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

def isoctal(n):
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
		print "octal"
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


a="0x123"
print isoctal(a),isnum(a),isstr(a),ischar(a)