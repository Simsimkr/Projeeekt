import random
from random import choice, randint
import rooms

max_hp = 1000
max_mana = 500
mana = 500
hp = 666

big_heal_potion = 5
small_heal_potion = 10
big_mana_potion = 5
small_mana_potion = 10

atak = [1,2,3,4,5,6,7,8,9]

rozmiary = ['Sredni', 'Maly', 'Durzy']


f_oponents = ['slime', 'wilk', 'goblin', 'org', 'golem']
s_oponents = ['dron', 'robot', 'robopolicyant', 'robot ninja', 'robot zabujca']
r_oponents = ['szczyr', 'pies', 'bangyta', 'zbieracz podatkuw', 'SSman']
liczba_pokonanych_przeciwnikow = 0


def random_oponent(styl):
    rozmiar = choice(rozmiary)
    op = []
    op.append(rozmiar)

    i = 0
    if styl == 'fantasy':
        oponent = choice(f_oponents)
        for list_object in f_oponents:
            if list_object == oponent:
                positon = i
    elif styl == 'si-fi':
        oponent = choice(s_oponents)
        for list_object in s_oponents:
            if list_object == oponent:
                positon = i
            i += 1
    elif styl == 'rzecywistosc':
        oponent = choice(r_oponents)
        for list_object in r_oponents:
            if list_object == oponent:
                positon = i

    op.append(oponent)

    if rozmiar == 'Sredni':
        op_hp = 0
        op_d = 0
    elif rozmiar == "Maly":
        op_hp = -25
        op_d = -10
    elif rozmiar == "Durzy":
        op_hp = 25
        op_d = 10

    if positon == 0:
        op_hp = op_hp + 26
        op_d = op_d + 15
    elif positon == 1:
        op_hp = op_hp + 50
        op_d = op_d + 30
    elif positon == 2:
        op_hp = op_hp + 75
        op_d = op_d + 45
    elif positon == 3:
        op_hp = op_hp + 100
        op_d = op_d + 60
    elif positon == 4:
        op_hp = op_hp + 125
        op_d = op_d + 75
    elif positon == 5:
        op_hp = op_hp + 150
        op_d = op_d + 90

    op.append(op_hp)
    op.append(op_d)
    return op


def fight(styl):
    global big_heal_potion, big_mana_potion, small_heal_potion, small_mana_potion
    opponent = random_oponent(styl)
    global hp, liczba_pokonanych_przeciwnikow
    while opponent[2] > 0 and hp > 0:
        print(f"walczysz teraz z {opponent[0]} {opponent[1]}")
        print(f"Przeciwnik ma {opponent[2]} HP i zadaje Ci {opponent[3]} obrażeń")

        hp -= opponent[2]
        if hp <= 0:
            break

        print(f"Masz {hp} HP i {mana} many")
        atak = wybierz_atak()
        opponent[2] -= atak
        print(f"Zadałeś {atak} obrażeń")

    if opponent[2] <= 0:
        print('Zabiłeś przeciwnika!!!')
        a = random.randint(1, 100)
        potions = ['heal_potion', "mana_potion"]
        if a >= 67:
            potion = choice(potions)
            a = random.randint(1, 100)
            if a >= 60:
                rozmiar = 'big'
            elif a < 60:
                rozmiar = 'smoll'
            if potion == "heal_potion":
                if rozmiar == 'big':
                    big_heal_potion += 1
                    print("Znalazlesz big heal potion!")
                    print(f'Teraz masz {big_heal_potion} big heal potion')
                elif rozmiar == 'smoll':
                    small_heal_potion += 1
                    print("Znalazlesz small heal potion!")
                    print(f'Teraz masz {small_heal_potion} small heal potion')
            elif potion == 'mana_potion':
                if rozmiar == 'big':
                    big_mana_potion += 1
                    print("Znalazlesz big heal potion!")
                    print(f'Teraz masz {big_mana_potion} big mana potion')
                elif rozmiar == 'smoll':
                    small_heal_potion += 1
                    print("Znalazlesz small heal potion!")
                    print(f'Teraz masz {small_mana_potion} small mana potion')
        liczba_pokonanych_przeciwnikow += 1


def wybierz_atak():
    a = True
    while a:
        print('a/A - atak')
        print('b/B - Atak specjalny')
        print(f'c/C - heal potion')
        print(f'd/D - mana potion')
        co = input().upper()
        if co == 'A':
            a = False
            return atak()
        elif co == 'B':
            a = False
            return specjal_atak()
        elif co == 'C':
            healing()
        elif co == 'D':
            maning()
        else:
            print("Nie wybrano akcji")


def atak():
    a = random.randint(1, 100)
    if a >= 75:
        print('Critikal atak')
        return randint(100, 500)
    else:
        return randint(1, 100)


def specjal_atak():
    global big_heal_potion, big_mana_potion, small_heal_potion, small_mana_potion
    global mana, hp
    a = [1, 2, 3, 4, 5, 6, 7]
    ch = choice(a)
    if mana < 50:
        print("-" * 40)
        print("Nie masz wystarczającej ilości many!")
        return 0
    elif mana >= 50:
        mana -= 50
        if ch == 1:
            print('Znalazlesz potke')
            potions = ['heal_potion', "mana_potion"]
            potion = choice(potions)
            a = random.randint(1, 100)
            if a <= 60:
                rozmiar = 'big'
            elif a > 60:
                rozmiar = 'smoll'
            if potion == "heal_potion":
                if rozmiar == 'big':
                    big_heal_potion += 1
                    print("Znalazlesz big heal potion!")
                    print(f'Teraz masz {big_heal_potion} big heal potion')
                elif rozmiar == 'smoll':
                    small_heal_potion += 1
                    print("Znalazlesz small heal potion!")
                    print(f'Teraz masz {small_heal_potion} small heal potion')
            elif potion == 'mana_potion':
                if rozmiar == 'big':
                    big_mana_potion += 1
                    print("Znalazlesz big heal potion!")
                    print(f'Teraz masz {big_mana_potion} big mana potion')
                elif rozmiar == 'smoll':
                    small_heal_potion += 1
                    print("Znalazlesz small heal potion!")
                    print(f'Teraz masz {small_mana_potion} small mana potion')
            return 0
        elif ch == 2:
            l = ['wybuch', 'blyskawica', 'kamienia', 'g*wno']
            ch = choice(l)
            print(f'Rzucasz [{ch}]')
            ud = random.random()
            x = random.randint(100, 500)
            if ud >= 0.5:
                print("udana")
                return x
            else:
                print('nie udana')
                hp -= x
                return 0
        elif ch == 3:
            print("zabijasz przyciwnika")
            return 10000000000000000000000
        elif ch == 4:
            print('Uleczyesz sie')
            x = random.randint(1, 500)
            hp += x
            print(f"Uleczylesz {x} hp")
            if hp >= max_hp:
                hp = max_hp
                print('masz Max HP')
            print(f'Teraz masz {hp} hp')
            return 0
        elif ch == 5:
            x = randint(1, 100)
            if x <= 90:
                print("bylesz blisko smierci")
                return 0
            elif x > 90:
                print("umierasz")
                hp = 0
                end("bad")
                return 0
        elif ch == 6:
            print('Straciesz potke')
            potions = ['heal_potion', "mana_potion"]
            potion = choice(potions)
            a = random.randint(1, 100)
            if a <= 60:
                rozmiar = 'big'
            elif a > 60:
                rozmiar = 'smoll'
            if potion == "heal_potion":
                if rozmiar == 'big' and big_heal_potion > 0:
                    big_heal_potion -= 1
                    print("Straciesz big heal potion!")
                    print(f'Teraz masz {big_heal_potion} big heal potion')
                elif big_heal_potion <= 0:
                    print('Okazalo sie rze nie masz tej potki kturej mialesz stracic')
                elif rozmiar == 'smoll' and small_heal_potion > 0:
                    small_heal_potion -= 1
                    print("Straciesz small heal potion!")
                    print(f'Teraz masz {small_heal_potion} small heal potion')
                elif small_heal_potion <= 0:
                    print('Okazalo sie rze nie masz tej potki kturej mialesz stracic')
            elif potion == 'mana_potion':
                if rozmiar == 'big' and big_mana_potion > 0:
                    big_mana_potion -= 1
                    print("Straciesz big heal potion!")
                    print(f'Teraz masz {big_mana_potion} big mana potion')
                elif big_mana_potion <= 0:
                    print('Okazalo sie rze nie masz tej potki kturej mialesz stracic')
                elif rozmiar == 'smoll' and small_mana_potion > 0:
                    small_heal_potion -= 1
                    print("Straciesz small heal potion!")
                    print(f'Teraz masz {small_mana_potion} small mana potion')
                elif big_heal_potion <= 0:
                    print('Okazalo sie rze nie masz tej potki kturej mialesz stracic')
            return 0
        elif ch == 7:
            print("To koniec")
            end("good")
            return 0


def healing():
    global hp, big_heal_potion, small_heal_potion
    a = True
    while a:
        print(f'b/B - big potion. masz {big_heal_potion}')
        print(f's/S - small potion. masz {small_heal_potion}')
        print(f'e/E  - exit')
        x = input().upper()
        if x == 'B':
            if big_heal_potion == 0:
                print("nie masz big heal potion")
                a = False
            elif big_heal_potion > 0 and hp < max_hp:
                big_heal_potion -= 1
                hp += 250
                print("Uleczylesz 250 hp")
        elif x == 'S':
            if small_heal_potion == 0:
                print("nie masz small heal potion")
            elif small_heal_potion > 0 and hp < max_hp:
                small_heal_potion -= 1
                hp += 175
                print("Uleczylesz 175 hp")
        elif x == 'E':
            a = False
        else:
            print(print("Nie wybrano akcji"))
        if hp >= max_hp:
            hp = max_hp
            print('masz Max HP')
    print(f'Teraz masz {hp} hp')


def maning():
    global mana, big_mana_potion, small_mana_potion
    a = True
    while a:
        print(f'b/B - big potion. masz {big_mana_potion}')
        print(f's/S - small potion. masz {small_mana_potion}')
        print(f'e/E  - exit')
        x = input().upper()
        if x == 'B':
            if big_mana_potion == 0:
                print("nie masz big mana potion")
                a = False
            elif big_mana_potion > 0 and mana < max_mana:
                big_mana_potion -= 1
                mana += 100
                print("Otrzymalesz 100 many")
        elif x == 'S':
            if small_mana_potion == 0:
                print("nie masz small heal potion")
            elif small_mana_potion > 0 and mana < max_mana:
                small_mana_potion -= 1
                mana += 50
                print("Otrzymalesz 50 many")
        elif x == 'E':
            a = False
        else:
            print(print("Nie wybrano akcji"))
        if mana >= max_mana:
            mana = max_mana
            print('masz Max mana')
    print(f'Teraz masz {mana} mna')


def end(end):
    if end == "bad":
        print("smutny koniec")
        print('Umarlesz, ale umarlesz walcac')
    elif end == "good":
        print("Jak dotarlesz konca -- sdecyduj sei:\n"
              "czy staniesz panowac nad CHAOSEM -- czy stracisz jego moc")
        a = True
        while a:
            print("a/A -- panowac")
            print("b/B -- stracic")
            b = input().upper()
            if b == 'A':
                print("Zostajesz poslancem CHAOSU")
                a = False
            elif b == 'B':
                print("To wszystko okazalo sie snem psa :)")
                a = False
            else:
                print("wybieraj")
    while True:
        x = input()
        print('To naprawde koniec, odejsc s tad!!!!!!!!!!!!!!!!!!!')

style = ["fantasy", "si-fi", "rzecywistosc"]

def game():
    print('Jednego ranku obudzilesz sie z niesamowita moca HAOSU. Jedynie co, nie umiesz jej kontrolowac \n'
          'Morze pomuc tobie, a morze i zabic.\n'
          'Twoje rzycie przetworzylo sie w nieskanczony lancug korytarzy, w kturych ciagle musisz walczyc za swoje rzycie.\n'
          'Ale gdy jurz stracilesz chec do rzycia, jestesz gotuw sie potdac – slyszysz glos w swej glowie.\n'
          'Ten glos jest glosem HAOSU\n'
          'Muwi tobie rze jesli przejdzesz przez 100 pokojuw, 100 walk, to bedziesz mugl wybierac\n'
          'A co to znacz, domysl sie sam\n'
          'Z nowa sila wchodzisz do pokoju I ….')

    while hp > 0:
        styl = choice(style)
        print("-" * 40)
        rooms.pokuj(styl)
        fight(styl)
        if liczba_pokonanych_przeciwnikow == 100:
            end('good')
        elif hp <= 0:
            end('bad')
    print(f'Liczba pok p == {liczba_pokonanych_przeciwnikow}')