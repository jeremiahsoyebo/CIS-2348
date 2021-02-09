

print('Enter amount of lemon juice (in cups):')
LemonJuice = float(input())
print('Enter amount of water (in cups):')
Water = float(input())
print('Enter amount of agave nectar (in cups):')
AgaveNectar = float(input())
print('How many servings does this make?\n')
ServingsMade = float(input())


print('Lemonade ingredients - yields', '{:.2f}'.format(ServingsMade), 'servings')
print('{:.2f}'.format(LemonJuice), 'cup(s) lemon juice')
print('{:.2f}'.format(Water), 'cup(s) water')
print('{:.2f}'.format(AgaveNectar), 'cup(s) agave nectar\n')


print('How many servings would you like to make?\n')
ServingsDesired = float(input())

DesiredConversion = ServingsDesired / ServingsMade
DesiredLemonJuice = LemonJuice * DesiredConversion
DesiredWater = Water * DesiredConversion
DesiredAgave = AgaveNectar * DesiredConversion
print('Lemonade ingredients - yields', '{:.2f}'.format(ServingsDesired), 'servings')
print('{:.2f}'.format(DesiredLemonJuice), 'cup(s) lemon juice')
print('{:.2f}'.format(DesiredWater), 'cup(s) water')
print('{:.2f}'.format(DesiredAgave), 'cup(s) agave nectar\n')

gallonLemonJuice = DesiredLemonJuice / 16.00
gallonWater = DesiredWater / 16.00
gallonAgave = DesiredAgave / 16.00

print('Lemonade ingredients - yields', '{:.2f}'.format(ServingsDesired), 'servings')
print('{:.2f}'.format(gallonLemonJuice), 'gallon(s) lemon juice')
print('{:.2f}'.format(gallonWater), 'gallon(s) water')
print('{:.2f}'.format(gallonAgave), 'gallon(s) agave nectar')
