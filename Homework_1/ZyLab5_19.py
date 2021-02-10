print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

print('Select first service:')
firstService = input()
print('Select second service:\n')
secondService = input()

services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}
print("Davy's auto shop invoice\n")
if firstService == 'Oil change':
    print('Service 1: Oil change, $35')
elif firstService == 'Tire rotation':
    print('Service 1: Tire rotation, $19')
elif firstService == 'Car wash':
    print('Service 1: Car wash, $7')
elif firstService == 'Car wax':
    print('Service 1: Car wax, $12')
elif firstService == '-':
    print('Service 1: No service')

if secondService == 'Oil change':
    print('Service 2: Oil change, $35')
elif secondService == 'Tire rotation\n':
    print('Service 2: Tire rotation, $19\n')
elif secondService == 'Car wash':
    print('Service 2: Car wash, $7\n')
elif secondService == 'Car wax':
    print('Service 2: Car wax, $12\n')
elif secondService == '-':
    print('Service 2: No service\n')

print('Total: ${}'.format(services[firstService] + services[secondService]))
