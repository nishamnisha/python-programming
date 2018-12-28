import sys
def gcd2():
	(x1,y1)=map(int,sys.stdin.readline().split())
	while(y1!=0):
		t=y1
		y1=x1%y1
		x1=t
	print(x1)
try:
	gcd2()
except:
	print('invalid')
