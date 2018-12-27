o = int(input())
assert 1<=o<=9999999
c = [str(i) for i in range(1,o+1)]
d = ''.join(c)
print(len(d))
