import random
def kaartenDek():
    dek = list()
    for i in range(0,54):
        randomChoice = random.randint(0,54)
        dek.append(kleuren[randomChoice])
    return dek
jokers = ['joker,', 'Joker,']
dek = list()
kleuren = ['Klaveren ', 'Harten ', 'Schoppen ', 'Ruiten ']
cijfer = ['1,','2,','3,','4,','5,','6,','7,','8,','9,','10,','Boer,','Vrouw,','Heer,','Aas,']
for x in range (0,len(kleuren)):
    for y in range(0,len(cijfer)):
        dek.append(kleuren[x]+cijfer[y])
dek.append(jokers[0]);dek.append(jokers[1])
randomdek = list()
for x in range(0,len(dek)):
    randomnummer = random.randint(0,len(dek))
    randomdek.append(dek[randomnummer-1])
    dek.remove(dek[randomnummer-1])
startKaarten = (randomdek[0],randomdek[1],randomdek[2],randomdek[3],randomdek[4],randomdek[5],randomdek[6])
for lijstje in startKaarten:
    print(lijstje)
print()
printKaarten= ''
for x in range(7,54):
    printKaarten += randomdek[x]+" "
print(printKaarten)


