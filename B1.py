f = open("B1.INP", "r")
f1 = open("B1.OUT", "w")
a = f.readlines()
f1.write(str(int(a[1]) + int(a[0])))
f1.write("\n")
f1.write(str(int(a[1]) - int(a[0])))
f1.write("\n")
f1.write(str(int(a[1]) * int(a[0])))
f1.write("\n")
f1.write(str(int(a[1]) / int(a[0])))
f.close()
f1.close()
