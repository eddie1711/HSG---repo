dt,dl,dh = float(input()),float(input()),float(input())
tong = dt + dl + dh
tb = tong / 3
print(tong)
print(tb)
if tb >= 0 and tb < 2:
    print("Loai kem")
elif tb >= 2 and tb < 5:
    print("Loai yeu")
elif tb >= 5 and tb < 6.5:
    print("Loai trung binh")
elif tb >= 6.5 and tb < 8:
    print("Loai kha")
else:
    print("Loai gioi")
