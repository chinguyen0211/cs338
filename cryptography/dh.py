g = 11
p = 59

failed_a = []
failed_b = []

def carmichael():
    a = 0
    b = 0
    while (g**a % 59) != 57 and a not in failed_a :
        a+=1

    while (g**b % 59) != 44 and b not in failed_b:
        b+=1

    return (a,b)

while (11**carmichael()[0]%59)**carmichael()[1]%59 != (11**carmichael()[1]%59)**carmichael()[0]%59 :
    failed_a.append(carmichael[0])
    failed_b.append(carmichael[1])
    carmichael()

sharedK = (11**carmichael()[0]%59)**carmichael()[1]%59
print("The shared secret is: ", sharedK)
