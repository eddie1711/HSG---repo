tt = int(input())
smt = 0
if tt < 6000000:
    print("Khong dong thue")
elif tt >= 6000000 and tb < 9000000:
    smt = (tt * 0.02) + tt
elif tt >= 9000000 and tb < 12000000:
    smt = (tt * 0.03) + tt
else:
    smt = (tt * 0.045) + tt
print(smt)
