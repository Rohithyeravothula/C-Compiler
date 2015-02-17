d=1
		for u in range(j,r):
			if u not in t and '^' not in first_val[nt.index(x[j])]:
				d=1
		if d==1:
			print "recursion at" ,g[i]
			a=a+follow(h[i])

for j in range(1,r+1):
			if s==x[r-j]:
				break


				if d==1 and s[j-1] not in t:
			print "adding ",dummy_follow[nt.index(h[i])],dummy_follow[nt.index(s[j-1])]
			dummy_follow[nt.index(s[j-1])]=dummy_follow[nt.index(s[j-1])]+dummy_follow[nt.index(h[i])]
