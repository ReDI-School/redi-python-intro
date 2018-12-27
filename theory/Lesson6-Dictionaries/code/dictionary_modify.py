# Lesson6: Dictionaries
# source: code/dictionary_modify.py

grades = {}

finish = 'no'

while finish != 'yes':
    subject = input('Please enter the name of a subject:\n')
    grade = int(input('Please enter the grade:\n'))

    grades[subject] = grade

    for key in grades:
        print(key, ':', grades[key])

    finish = input('Do you want to quit the program? (type "yes" or "no"):\n').lower()