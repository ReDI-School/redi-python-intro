# Lesson5: reading file contents twice
# source: code/file_read_twice.py

f = open('file_for_reading.txt', 'r')

text = f.read()
print(text)

print("\nNow reading for a second time: ")

text_copy = f.read()
print(text_copy)

f.close()