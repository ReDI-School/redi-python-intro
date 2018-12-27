# Lesson5: changing current position
# source: code/file_seek.py

f = open('file_for_reading.txt', 'r')

text = f.read()
print(text)

print("\nNow reading for a second time:\n")

f.seek(0)

text_copy = f.read()
print(text_copy)

f.close()