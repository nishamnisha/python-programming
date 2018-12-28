import sys
 def getl():
	l1=[]
	r1=[]
	while(True):
		try:
			a,b = map(int,sys.stdin.readline().split())
		except ValueError:
			break
		l1.append(a)
		l1.append(b)
		r1.append(l1)
		l1=[]
	for i in r1:
		print(i[1]-i[0])
try:
	getl1()
except:
	print('invalid')
