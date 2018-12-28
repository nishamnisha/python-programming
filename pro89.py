def lex():
	s=input()
	l1=list(s)
	l1.sort()
	c=''.join(l1)
	print(c)
try:
	lex()
except:
	print('invalid')

