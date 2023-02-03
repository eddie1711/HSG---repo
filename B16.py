import math
f = open("B16.INP","r")
f1 = open("B16.OUT","w")
a = int(f.read())
def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
if isPrime(a) == True:
    f1.write("So nguyen duong la so nguyen to")
else:
    f1.write("So nguyen duong khong la so nguyen to")
f.close()
f1.close()
