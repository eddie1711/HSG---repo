a ,b = int(input()),int(input())
if a == 0 or b == 0 :
    UCLN = 0
else:
    t = b % a
    while t != 0:
        t = a % b 
        a = b 
        b = t
    UCLN = a
print(UCLN)
