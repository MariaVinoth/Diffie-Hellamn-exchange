import random

p=17
g=13

#randomly generating secret numbers for SA and SB
SA = random.randint(1,21)
SB = random.randint(1,21)

print("P:{} \n g:{}".format(p,g))
print("Random numbers: \n SA:{} \n SB:{}".format(SA,SB))

TA = (g**SA) % p
TB = (g**SB) % p


TA1 = (TB**SA) % p
TB1 = (TA**SB) % p

if TA1 == TB1:
    print("{} is the secret number!" .format(TA1))








