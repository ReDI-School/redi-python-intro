# Lesson3: for loop over a string
# source: code/for_string.py

s = 'this is a random string with several letters \'a\''
counter = 0
for character in s:
    if character == 'a':
        counter += 1
print('Found', counter, 'letters \'a\' in the given string')