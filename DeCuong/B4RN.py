tb = float(input())
if tb < 2:
    if tb >= 0:
        print("Loai kem")
elif tb < 5:
    if tb >= 2:
        print("Loai yeu")
elif tb < 6.5:
    if tb >= 5:
        print("Loai trung binh")
elif tb < 8:
    if tb >= 6.5:
        print("Loai kha")
else:
    print("Loai gioi")
