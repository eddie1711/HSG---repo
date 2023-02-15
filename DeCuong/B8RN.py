nam = int(input())
if nam % 400 == 0 or nam % 4 == 0 and nam % 100 != 0:
    print("366 ngay")
else:
    print("365 ngay")
