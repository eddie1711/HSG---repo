f = open("B2.INP","r")
f1 = open("B2.OUT","w")
a = f.readlines()
f1.write(str(int(a[0]) // int(a[1])) + "\n")
f1.write(str(int(a[0]) % int(a[1])))
f.close()
f1.close()
