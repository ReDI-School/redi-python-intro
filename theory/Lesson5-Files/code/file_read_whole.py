# Lesson5: reading all the file at once
# source: code/file_read_whole.py

f = open('file_for_reading.txt', 'r')

text = f.read()
print(text)

f.close()