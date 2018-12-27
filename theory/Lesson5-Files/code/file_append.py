# Lesson5: appending to a file
# source: code/file_append.py

with open('test.txt', 'a') as f:
    f.write('New line at the end of a file\n')
