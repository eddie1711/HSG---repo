a = int(input())
b = []
print(bin(a))
while a != 0:
    smt = a % 2
    b.append(smt)
    a = a//2
b.reverse()
print(b)
