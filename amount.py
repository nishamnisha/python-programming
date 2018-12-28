import math

def min3(n1,n2,n3):
    if n1<= n2 and n1<= n3:
        return n1
    elif n2<= n1 and n2<= n3:
        return n2
    elif n3<= n2 and n3<= n1:
          return n3
print(min3(4, 7, 5))

print(min3(4, 5, 5))

print(min3(4, 4, 4))

print(min3(-2, -6, -100))

print(min3("Z", "B", "A"))

