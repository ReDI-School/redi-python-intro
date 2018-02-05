
#print('Please enter length')

length = input('Please enter length')

#print('Please enter width')

width = input('Please enter width')

choice = input('Enter 1 for area/2 for perimeter')

if(choice == 1):
    area = length * width
    print('Area: ',area)
elif(choice == 2):
    perimeter = 2 * (length + width)
    print('Perimeter: ', perimeter)
else:
    print('invalid input')

