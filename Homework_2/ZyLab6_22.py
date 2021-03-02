# Jeremiah Soyebo - 1902930 #

a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())


def function1(x, y):
    return a * x + b * y - c


def function2(x, y):
    return d * x + e * y - f


xSolution = 0
ySolution = 0
for x in range(-10, 11):
    for y in range(-10, 11):
        if function1(x, y) == function2(x, y) and function2(x, y) == 0:
            xSolution = x
            ySolution = y
if xSolution != 0 and ySolution != 0:
    print(xSolution, ySolution)
else:
    print('No solution')
