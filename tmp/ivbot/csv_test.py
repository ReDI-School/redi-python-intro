import csv

print('CSV VERSION')
with open('cities.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['city'], row['country'])

print('FILE VERSION')
file = open('cities.csv', 'r')
line_number = 1
for line in file:
    if line_number > 1:
        data = line.split(',')
        print( data[0], data[2].rstrip() )
    line_number += 1

cities_list = []
with open('cities.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for r in reader:
        print(r)
        cities_list.append(r)
print(cities_list)

