st=input("Enter the string:")
l1=len(st)
st1=list(st)
k1=round(l1//2)
st1[k1]='*'
ans=''
for x in st1:
	ans=ans+x
print(ans)
