# Lesson6: Sets
# source: code/sets_operations.py

# Input data
python_languages = ['russian', 'french', 'arabic', 'arabic', 'arabic', 'arabic', 'farsi']
java_languages = ['english', 'kurdish', 'arabic', 'arabic', 'french']

# How many different languages do we have in each class?
python_set = set(python_languages)
java_set = set(java_languages)
print('Python:', len(python_set), 'Java:', len(java_set))

# What are the languages spoken in both classes?
print('All languages:', python_set | java_set)

# What are common languages between the two classes?
print('Common languages:', python_set & java_set)

# What are the languages that are found in only one class (not in both)?
print('One-class languages:', python_set ^ java_set)

# What are languages found in Python class but not in Java class?
print('Python class specific languages:', python_set - java_set)
