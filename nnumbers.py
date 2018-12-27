def m_String(m, l):
n = len(m)

fre = [0] * 26

for i in range(n):
fre[ord(m[i]) – ord(‘a’)] += 1

str = “”

for i in range( 26) :

if (fre[i] % l == 0) :
x = fre[i] 

while (x) :
str += chr(i + ord(‘a’))
x -= 1

else :
return “-1”

return str
if __name__ == “__main__”:

m = “aabb”
l = 2

print( l_String(m, l))

