import random

nummers = ['1','2','3','4','5','6']
dobbelstenen = []

def dobbelen ():
    print ('Hier zijn uw gedobelde dobbelstenen:\n')
    for i in range (5):
        dobbelsteen = random.choice(nummers)
        dobbelstenen.append (dobbelsteen)
    print (dobbelstenen)
    apartzetten = input ('Wil je dobbel stenen apart zetten? JA / NEE : ').upper()
    if apartzetten == ('JA'):
        
    if apartzetten == ('NEE'):

    
def yathzee():
    for i in range (1):
        print('\nWelkom bij Yahtzee ')
        startspel = input('\nWilt u beginnen: Ja/Nee ').upper()
        if startspel == ('JA'):
            dobbelen()
        if startspel == ('NEE'):
            break





yathzee()