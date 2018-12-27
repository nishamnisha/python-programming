num1 = int(input('How many numbers: '))
total_sum = 0
for m in range(num1):
    numbers = float(input('Enter number : '))
    total_sum += numbers
avg = total_sum/num1
print('Average of ', num1, ' numbers is :', avg)

