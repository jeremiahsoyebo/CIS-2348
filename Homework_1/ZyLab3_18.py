print('Enter wall height (feet):')
wallHeight = int(input())
print('Enter wall width (feet):')
wallWidth = int(input())
wallArea = wallWidth * wallHeight
print('Wall area:', wallArea, 'square feet')

gallonsNeeded = wallArea / 350.0
print('Paint needed:', '{:.2f}'.format(gallonsNeeded), 'gallons')
cansNeeded = round(gallonsNeeded)
print('Cans needed:', cansNeeded, 'can(s)\n')

print('Choose a color to paint the wall:')
wallColor = input()
colorPrices = {'Red': 35, 'Blue': 25, 'Green': 23, 'red': 35, 'blue': 25, 'green': 23}
paintCost = cansNeeded * (colorPrices[wallColor])

print('Cost of purchasing {} paint: ${}'.format(wallColor, paintCost))
