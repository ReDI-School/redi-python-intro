# Lesson6: Dictionaries
# source: code/dictionary_add.py

grades = {}

subject = input('Please enter the name of a subject:\n')
grade = int(input('Please enter the grade:\n'))

grades[subject] = grade

for key in grades:
    print(key, ':', grades[key])