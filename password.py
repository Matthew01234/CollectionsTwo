import random

letters = ['a','b', 'c', 'd' ,'f', 'g', 'h', 'i', 'j' ,'k', 'l' ,'m', 'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u', 'v' ,'w', 'x' ,'y', 'z']
hoofdletters = ['A','B', 'C', 'D' ,'F', 'G', 'H', 'I', 'J' ,'K', 'L' ,'M', 'N' ,'O' ,'P' ,'Q' ,'R' ,'S' ,'T' ,'U', 'V' ,'W', 'X' ,'Y', 'Z']
specialtekens = ['@' ,'#' ,'$', '%' ,'&', '_', '?','.']
nummers = ['1' ,'2' ,'3', '4' ,'5','6', '7','7','9','10']
wachtwoord = list()

hoeveelheidhoofdletters = ['2' ,'3' ,'4', '5' ,]
gekozenhoeveelheidhoofdletter = random.choice(hoeveelheidhoofdletters)

hoeveelheidcijfers =['4' ,'5' ,'6', '7' ,]
gekozenhoeveelheidcijfers =  random.choice(hoeveelheidcijfers)

for i in range(int(gekozenhoeveelheidhoofdletter)):
    wachtwoord.append(random.choice(hoofdletters))
for i in range(int(gekozenhoeveelheidcijfers)):
    wachtwoord.append(random.choice(nummers))
for i in range(3):
    wachtwoord.append(random.choice(specialtekens))
while len(wachtwoord)  != 24:
    wachtwoord.append(random.choice(letters))

x = True
while x == True:
    if wachtwoord[0] in specialtekens or wachtwoord[23] in specialtekens or wachtwoord[0] in letters or wachtwoord[1] in nummers or wachtwoord[2] in nummers:
        random.shuffle(wachtwoord)
    else: print(), print(*wachtwoord, sep="");x = False,   print()