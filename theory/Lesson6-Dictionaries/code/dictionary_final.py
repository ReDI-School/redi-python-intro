# Lesson6: Dictionaries
# source: code/dictionary_modify.py

grades = {}

finish = 'no'
while finish != 'yes':
    action = int(input('Please type "1" for reading the data and "2" for modifying:\n'))

    if action == 1:
        subject = input('Please enter the name of a subject:\n')

        if subject in grades:
            print('The grade is:', grades[subject])
        else:
            print('No such subject')
    elif action == 2:
        subject = input('Please enter the name of a subject:\n')
        grade = int(input('Please enter the grade:\n'))

        grades[subject] = grade

        for key in grades:
            print(key, ':', grades[key])
    else:
        print('Wrong input')

    finish = input('Do you want to quit the program? (type "yes" or "no"):\n').lower()