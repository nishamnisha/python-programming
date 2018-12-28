import math
def primes_till_n1(n1):
    sieve=[True]*n1
    for i in xrange(3,int(n1**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n1-i*i-1)/(2*i)+1)
    return [2]+[i for i in xrange(3,n1,2) if sieve[i]]

n1,l,r=map(int,raw_input().split())
primes=primes_till_n1(n1+1)
ct=0
for i in xrange(l,r+1):
    for j in primes:
        if i%j==0:
            ct+=1
            break
print ct

