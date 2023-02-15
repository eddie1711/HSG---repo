f = open("B17.INP","r")
f1 = open("B17.OUT","w")
a = f.readlines()
t = int(a[1]) % int(a[0])
b = int(a[0])
c = int(a[1])
while t != 0:
    t = b % c
    b = c
    c = t
f1.write(str(b))
f.close()
f1.close()
