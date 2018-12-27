# Lesson2: Nested conditions
# source: code/nested_conditions.py

age = int(input('Enter your age:\n'))
hour = int(input('What is the hour? (0-24)\n'))

is_late = hour >= 22
is_too_young = age <= 12

if is_late:
    if is_too_young:
        print('You should be sleeping ...')
    else:
        print('Want to watch a movie?')
else:
    print('Go for a walk!')
