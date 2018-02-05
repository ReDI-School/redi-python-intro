print('Enter first number')
num1 = input()
print('Enter second number')
num2 = input()

print('Enter third number')
num3 = input()

if(num1 >=num2) & (num1 >=num3):
    print(num1)
elif(num2 >=num1) and (num2>=num3):
    print(num2)
else:
    print(num3)