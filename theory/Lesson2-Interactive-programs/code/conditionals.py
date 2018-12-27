# Lesson2: Conditional operations
# source: code/conditionals.py

c = int(input('Enter degrees (c):\n'))

if c < 0:
    print("It's cold, stay at home")
elif c < 20:
    print("Put a jacket on")
else:
    print("It's a good weather for a T-shirt")
