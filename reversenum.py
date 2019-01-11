def rev():
	n1=int(input())
	rev=0
	while(n1!=0):
		r1=n1%10
		rev=rev*10+r1
		n1//=10
	print(rev)
try:
	rev()
except:
	print('invalid')
