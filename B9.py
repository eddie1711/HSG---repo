f = open("B9.INP","r")
f1 = open("B9.OUT","w")
a = int(f.read())
s = 0
for i in range(3):
    smt = a % 10
    s += smt
    a //= 10
f1.write(str(s))
f.close()
f1.close()
