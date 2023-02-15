tt = int(input())
smt = 0
if tt > 20000000:
    smt1 = tt * 0.04
    smt = smt1 + tt
elif tt > 50000000: 
    smt1 = tt * 0.055
    smt = smt1 + tt
elif tt > 100000000: 
    smt1 = tt * 0.065
    smt = smt1 + tt
elif tt < 20000000:
    smt1 = 0
    smt = tt
print(smt, smt1)
