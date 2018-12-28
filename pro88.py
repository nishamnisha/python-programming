def lcm2():
	(x1,y1)=map(int,sys.stdin.readline().split())
	temp=min(x1,y1)
	while(True):
		if temp%x1==0 and temp%y1==0:
			break
		temp+=1
	print(temp)
try:
	lcm2()
except:
	print('invalid')
