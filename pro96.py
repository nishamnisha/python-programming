num1=int(input("Enter any number"))
f=0
for x in range(1,num1+1):
	if(num1%x==0):
		f=f+1
if(f>2):
	print("composite")
else:
        print("Not composite")
