f = open("B19.INP","r")
f1 = open("B19.OUT","w")
a = f.readlines()
for i in range(int(a[0])):
    for j in range(int(a[1])):
        f1.write("* ")
    f1.write("\n")
f.close()
f1.close()
