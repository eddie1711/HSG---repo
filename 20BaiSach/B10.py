f = open("B10.INP", "r")
f1 = open("B10.OUT", "w")
a = f.readlines()
a.sort()
f1.write(a[1])
f.close()
f1.close()
