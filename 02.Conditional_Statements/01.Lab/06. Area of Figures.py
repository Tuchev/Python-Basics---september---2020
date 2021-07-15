import math
type = input()
if type == "square":
    a = float(input())
    area = a * a
    print(f'{area: .3f}')
elif type == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f'{area: .3f}')
elif type == "circle":
    r = float(input())
    area = math.pi * r * r
    print(f'{area: .3f}')
elif type == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2
    print(f'{area: .3f}')