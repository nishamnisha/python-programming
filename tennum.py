m=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    m.append(b)
m.sort()
print("Largest element is:",m[n-1])
