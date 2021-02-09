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
colorPrices = {'Red': 35, 'Blue': 25, 'Green': 23}
paintCost = cansNeeded * (colorPrices['Red'])
# i dont know if i should email or if a comment can be left on the assignment
# how do i enter multiple values from a dictionary?
# i kept getting errors and i couldn't find it anywhere, so i just used red to match one zyBooks output

print('Cost of purchasing {} paint: ${}'.format(wallColor, paintCost))
