lst = []
num1 = int(input('How many numbers: '))
for i in range(num1):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))
