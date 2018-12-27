# Lesson3: List is mutable
# source: code/list_is_mutable.py

original_list = list(range(1, 6))
print(original_list)
new_list = original_list
new_list[2] = 128
print(original_list)
print(new_list)