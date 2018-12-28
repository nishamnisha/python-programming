def sumall():
	n1=int(input())
	l1=[]
	sum=0
	for i in range(n1):
		l1.append(int(input()))
		sum+=l1[i]
	print(sum)
try:
	sumall()
except:
	print('invalid')
