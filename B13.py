f = open("B13.INP","r")
f1 = open("B13.OUT","w")
a = int(f.read())
if a <= 100:
    f1.write(str(a*550 + a*550*(10/100)))
elif a > 100 and a <= 150:
    f1.write(str(((100*550)+((a-100)*750)) +(((100*550)+((a-100)*750))*(10/100))))
elif a > 150 and a <= 200:
    f1.write(str(((100*550)+(50*750) + ((a-150)*950)) + (((100*550)+(50*750) + ((a-150)*950))*(10/100))))
else:
    f1.write(str(((100*550)+(50*750) + (50*950) + ((a - 200) * 1350)) + (((100*550)+(50*750) + (50*950) + ((a - 200) * 1350)) * (10/100))))
f.close()
f1.close()
