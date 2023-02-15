import math
a,b,c = float(input()),float(input()),float(input())
delta = b**2 - 4 * a * c
if delta < 0:
    print("vo nghiem")
elif delta == 0:
    x = -b / (2*a)
    if x < 0:
        print("vo nghiem")
    elif x == 0:
        print("1 nghiem ", x)
    else:
        print("x1 ", x)
        print("x2 ", -x)
else:
    x1 = (-b - math.sqrt(delta))/(2*a)
    x2 = (-b + math.sqrt(delta))/(2*a)
    if x1 > 0 and x2 < 0:
        print("x1 ", math.sqrt(x1))
        print("x2 ", (-1) * math.sqrt(x1))
    elif x1 < 0 and x2 > 0:
        print("x1 ", math.sqrt(x2))
        print("x2 ", (-1) * math.sqrt(x2))
    elif x1 < 0 and x2 < 0:
        print("vo nghiem")
    else:
        print("x1 ", math.sqrt(x1))
        print("x2 ", (-1) * math.sqrt(x1))
        print("x3 ", math.sqrt(x2))
        print("x4 ", (-1) * math.sqrt(x2))
