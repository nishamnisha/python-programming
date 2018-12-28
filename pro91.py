import sys
def cuboid():
	l1,b1,h1=map(int,sys.stdin.readline().split())
	print(l1*b1*h1)
try:
	cuboid()
except:
	print('invalid')
