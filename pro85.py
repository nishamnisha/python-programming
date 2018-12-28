ip=input("Enter any String:")
even=''
odd=''
for x1 in range(1,len(ip)+1):
	if(x1%2==0):
		even=even+ip[x1-1]
	else:
		odd=odd+ip[x1-1]
print(odd," ",even)
