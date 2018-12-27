# Lesson3: another while loop example
# source: code/while_number.py

num = int(input('Give me a number:\n'))
counter = 0
while num > 0:
    num //= 2
    counter += 1
print('Your number contains', counter, 'twos')
