# Lesson6: Dictionaries
# source: code/dictionary_creation_improved.py

grades = {'Math': 5,'Science': 3, 'English': 10,'German': 6}

subject = input('Please enter the name of a subject:\n')

if subject in grades:
    print('The grade is:', grades[subject])
else:
    print('No such subject')

