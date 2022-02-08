boodschappenlijstje = set()

i = True
while i == True:        
    toevoeging = input ('Wat wilt u toevoegen? Type het zo: product,')
    boodschappenlijstje.add(toevoeging)
    opnieuw = input('als je opnieuw een item wilt toevoegen, klik dan op enter (voer iets in als je dat niet wil). ')
    if opnieuw != '':
        i = False


print(boodschappenlijstje)