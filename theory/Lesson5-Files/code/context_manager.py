# Lesson5: Automatically closing a file
# source: code/context_manager.py

with open('file_for_reading.txt', 'r') as f:
    text = f.read()

print(text)

