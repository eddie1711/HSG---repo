f = open("B18.INP","r")
f1 = open("B18.OUT","w")
a = int(f.read())
for i in range(a):
    f1.write("* ")
f.close()
f1.close()
