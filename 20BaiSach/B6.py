f = open("B6.INP","r")
f1 = open("B6.OUT","w")
a = f.readlines()
f1.write(str(int(a[0]) / int(a[1])))
f.close()
f1.close()
