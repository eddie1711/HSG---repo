import math
a,b,c = float(input()), float(input()), float(input())
delta = b**2 - 4 * a * c
if delta < 0:
    print("Vo nghiem")
elif delta == 0:
    print("Nghiem kep: ", -(b/(2*a)))
else:
    x1 = ((-(b) - math.sqrt(delta))/(2*a))
    x2 = ((-(b) + math.sqrt(delta))/(2*a))
    print("2 nghiem ", x1,x2)
