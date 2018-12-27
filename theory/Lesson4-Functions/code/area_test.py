# Lesson4: calling a function
# source: code/area_test.py


def calculate_area(radius):
    area = 3.14 * (radius ** 2)
    return area


area1 = calculate_area(10)
area2 = calculate_area(20)

print(area1, area2)