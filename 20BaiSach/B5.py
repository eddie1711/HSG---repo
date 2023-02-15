f = open("B5.INP", "r")
f1 = open("B5.OUT", "w")
pi = 3.14
a = int(f.read())
f1.write("S = "+str(pi * (a**2))+"\n")
f1.write("P = "+str(2 * pi * (a**2)))
f.close()
f1.close()
