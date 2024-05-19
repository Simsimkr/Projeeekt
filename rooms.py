from random import choice

go_in = ["Wchodzisz do",
         "Drzwi prowadzą cię do ",
         "Po przekroczeniu progu znajdujesz się w",
         "Po przejściu przez wąskie przejście otwiera się przed tobą",
         "Wkraczasz do"]
pokoje = ["Sala do przemuwienia", 'pokuj nauczycielski', 'piwnica', 'korytarz', 'ulica', "mily dom"]

f_material = ['deski 1000letniego duba', 'kamienie z gury Awuszka', 'samy pulnocny lod', 'magiczna magma', 'ziemia z pod Igdrasila']
s_material = ['metal iskrcy prandem', 'adamntit', 'ziemia z marsu', 'kamienia z Ksiarzyca', 'energi']
r_material = ['plastik', 'metal', 'beton', 'drewno', 'kamienia']

def pokuj(styl):
    b = choice(go_in)
    pokuj = choice(pokoje)
    if styl == "fantasy":
        sciany = choice(f_material)
        podloga = choice(f_material)
        kanapa = choice(f_material)
        stol = choice(f_material)
        krzeslo = choice(f_material)
    elif styl == "si-fi":
        sciany = choice(s_material)
        podloga = choice(s_material)
        kanapa = choice(s_material)
        stol = choice(s_material)
        krzeslo = choice(s_material)
    elif styl == "rzecywistosc":
        sciany = choice(r_material)
        podloga = choice(r_material)
        kanapa = choice(r_material)
        stol = choice(r_material)
        krzeslo = choice(r_material)
    print(f'{b} [{pokuj}]. W tym miejcu sciany sa zlozone z [{sciany}], a podoga z [{podloga}].\n'
          f'Dzisisz sie temu rzee kanapa jest zrobiona z [{kanapa}], stol z [{stol}].\n'
          f'postanawiasz ze styl tego pokoju jest {styl}\n'
          f'Widzisz swego przeciwnika siedzaccego na krzzeslie zrobionym z [{krzeslo}]')
    return styl
