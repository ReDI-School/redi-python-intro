# Lesson3: Lists
# source: code/lists.py

l1 = [1, 5, 0, 4]  # create a list
print(l1)
l1.sort()          # sort the list
print(l1)
l1.append('a')     # add an element
print(l1)
del l1[2]          # remove an element
print(l1)
print(len(l1))     # length of the list
print('The first element is', l1[1])
empty_list = []    # create an empty list
print(len(empty_list))
# create a list from range: [0-10)
l2 = list(range(10))
print(l2)
# create a list from range: [5-10)
l3 = list(range(5, 10))
print(l3)
