n1=int(input("Enter N value:"))
k1=int(input("Enter K value:"))
print("Enter the array values:")
a=[]
for x in range(0,n1):
	t=int(input())
	a.append(t)
print(a[k1-1])
