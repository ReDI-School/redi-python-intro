# Lesson4: example of variables scopes
# source: code/scope_example.py


def calculate_area(radius): # parameters are local variables
    area = pi * (radius ** 2)  # local variable, is not visible
                               # outside of the function
                               # and shadows global variable with the same name
    return area


pi = 3.14  # global variable - is visible in function if defined
           # before the first call of the function (try to move it
           # after the first call of calculate_area function )

area = 100  # global variable with the same name as local one in function

area1 = calculate_area(10)
area2 = calculate_area(20)

print(area1, area2)
print(area) # prints the one of the closest scope
print(radius) # Error here, there is no radius variable in the global scope
