# Lesson5: reading from a file line by line
# source: code/file_read_by_line.py

f = open('file_for_reading.txt', 'r')

for line in f:
    print(line)

f.close()