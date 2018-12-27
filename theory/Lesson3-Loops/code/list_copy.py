# Lesson3: Copy a list
# source: code/list_copy.py

original_list = list(range(1, 6))
print(original_list)
new_list = original_list.copy()
new_list[2] = 128
print(original_list)
print(new_list)