f = open("B14.INP","r")
f1 = open("B14.OUT","w")
a = f.read()
if a =="hai":
    f1.write("Sinh; Anh; Van; Van; Chao Co")
elif a =="ba":
    f1.write("Anh; Hoa; Hoa; Sinh")
elif a == "tu":
    f1.write("Nghi")
elif a == "nam":
    f1.write("Toan; Toan; Ly; Ly; Anh")
elif a == "sau":
    f1.write("Su; Ly; Hoa; Van; Sinh Hoat")
elif a == "bay":
    f1.write("Tin; Tin; Su; Toan; Toan")
else:
    f1.write("Nghi")
f.close()
f1.close()
