a,b,c = float(input()), float(input()),float(input())
a1,b1,c1 = float(input()), float(input()),float(input())
d = a * b1 - a1 * b
dx = c * b1 - b * c1
dy = a * c1 - c * a1
print("x = ", dx/d)
print("y = ", dy/d)
