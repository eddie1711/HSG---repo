import math
f = open("B4.INP", "r")
f1 = open("B4.OUT", "w")
a = f.readlines()
p = int(a[0]) + int(a[1]) + int(a[2])
f1.write(str(math.sqrt(p * (p - int(a[0])) * (p - int(a[1])) * (p - int(a[2])))))
f.close()
f1.close()
