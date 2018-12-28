 def odddig():
	n1=int(input())
	r=[]
	while(n1!=0):
		r.append(n1%10)
		n1//=10
	for i in range(len(r)-1,-1,-1):
		if r[i]%2!=0:
			print(r[i])
try:
	odddig()
except:
	print('invalid')

