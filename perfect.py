n1=int(input("Enter 1st number"))
n2=int(input("Enter 2nd number"))
flag=0
prod=n1*n2
for x in range(1,max(n1,n2)+1):
	k=x*x
	if k==prod:
		flag=1
if (flag==0):
	print("NO")
else:
	print("Yes")

