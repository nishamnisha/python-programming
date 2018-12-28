def isogram():
	s=input()
	l1=list(s)
	r1=[]
	for i in l1:
		if not i in r1:
			r1.append(i)
	if len(l1)==len(r1):
		print('yes')
	else :
		print('no')
try:
	isogram()
except:
	print('invalid')
