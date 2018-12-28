def si():
	(p1,n1,r1)=map(int,sys.stdin.readline().split())
	sii=p1*n1*r1/100
	print(math.floor(sii))
try:
	si()
except:
	print('invalid')
