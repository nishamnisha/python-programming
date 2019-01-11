def changed():
	n1=int(input())
	l1=[]
	for i in range(n1):
		l1.append(int(input()))
	for i in range(1,n1):
		if l1[i-1]>l1[i]:
			print(l1[i-1])
			break
try:
	changed()
except:
	print('invalid')
