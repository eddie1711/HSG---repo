import math
f = open("B11.INP","r")
f1 = open("B11.OUT","w")
a = f.readlines()
delta = int(a[1])**2 - 4*int(a[0])*int(a[2])
print(delta)
if delta < 0:
    f1.write("Phuong trinh vo nghiem")
elif delta == 0:
    f1.write("Phuong trinh co nghiem kep: "+str(-1*int(a[1])/(2*int(a[0]))))
else:
    x1 = ((-1*int(a[1])) + math.sqrt(delta)) / (2*int(a[0]))
    x2 = ((-1*int(a[1])) - math.sqrt(delta)) / (2*int(a[0]))
    f1.write("Phuong trinh co 2 nghiem: " + str(x1) + "\n" + str(x2)) 
f.close()
f1.close()
