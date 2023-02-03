f = open("B12.INP","r")
f1 = open("B12.OUT","w")
a = int(f.read())
if a >= 5:
    f1.write(str(450*a))
else:
    f1.write(str(500*a))
f.close()
f1.close()
