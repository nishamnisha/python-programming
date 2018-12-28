ip=input("Enter your seqence (Mod/Dividee):")
op=['%','/']
for x1 in ip:
	if x1 in op:
		if(x1=='%'):
			k1=int(ip.split(x1)[0])
			k2=int(ip.split(x1)[1])
			ans=k1%k2
		elif(x1=='/'):
			k1=int(ip.split(x1)[0])
			k2=int(ip.split(x1)[1])
			ans=k1//k2
print(ans)
