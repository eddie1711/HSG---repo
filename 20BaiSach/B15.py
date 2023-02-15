f = open("B15.INP","r")
f1 = open("B15.OUT","w")
a = int(f.read())
s = 1
for i in range(a,0,-1):
    s *= i
f1.write(str(s))
f.close()
f1.close()
