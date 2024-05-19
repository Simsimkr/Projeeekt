import copy
from random import choice, randint
from classes import Library, Book, Men
from bbb import game

autor = ["q", 'w', 'e', 'r', 't']
styl = ['horror', 'fantasy', 'school']
name = ['a', 's', 'd', 'f', 'g']

# b = Book(choice(name), choice(autor), choice(styl), randint(10, 3000), randint(1900, 2020))
m = 0


def finder(lis):
    print("Nazwa,autor,styl,dlugosc lub rok")
    k = input()
    if k == "nazwa":
        print("wprovadz nazwe:")
        v = input()
    elif k == "dlugosc":
        print("wprovadz dlugosc:")
        v = input()
    elif k == "styl":
        print("wprovadz styl:")
        v = input()
    elif k == "rok":
        print("wprovadz rok:")
        v = input()
    elif k == "autor":
        print("wprovadz autora:")
        v = input()
    elif k == "id":
        print("wprovadz id:")
        v = input()

    lis_out = []
    k = k.lower()
    v = str(v).lower()

    for el in lis:
        if k == "nazwa":
            if el.name.lower() == v:
                lis_out.append(el)
        elif k == "dlugosc":
            if el.dlugosc.lower() == v:
                lis_out.append(el)
        elif k == "styl":
            if el.styl.lower() == v:
                lis_out.append(el)
        elif k == "rok":
            if el.rok.lower() == v:
                lis_out.append(el)
        elif k == "autor":
            if el.autor.lower() == v:
                lis_out.append(el)
        elif k == "id":
            if el.autor.lower() == v:
                lis_out.append(el)

    i = 0
    for el in lis_out:
        el.infb()
        print(f'numer: {i}')
        i += 1
        print("*"* 90)

    return lis_out


def book_taker(lis):
    d = 1
    while d == 1:
        print("Wprowadz numer ksianzki")
        odp = input()
        try:
            odp = int(odp)
            d = 0
        except:
            print('nope')
    o = lis[odp]
    return o


def gen_day():
    global m
    lb = []
    m = 0
    for i in range(randint(1, 5 + m)):
        l = Library()
        for f in range(randint(5, 15 + m * 4)):
            l.add_book(Book(choice(name), choice(autor), choice(styl), randint(10, 3000), randint(1900, 2020)))
        lb.append(copy.deepcopy(l))

    return lb


def praca(lb):
    global score
    ex = False
    ok = 1

    while ok != 0 :
        print("chcesz wyjsc?")
        a = input()
        if a == "tak":
            break
        d = 1
        l = choice(lb)
        b = choice(l.books)
        men = Men(copy.deepcopy(b))
        print(f'Proszę książkę {men.marzenia[0]}: {men.marzenia[1]} i {men.marzenia[2]}: {men.marzenia[3]}')

        while d != 0:
            d = 1
            print(f"masz {len(lb)} bibliotek. W kturej szukasz")
            odp = input()
            if odp == 'ex':
                ex = True
            try:
                odp = int(odp)
                d = 0
            except:
                print('nope')

        l = lb[odp - 1]
        l_test = finder(l.books)
        f = 0

        while f == 0:

            if len(l_test) < 1:
               print("nima ksiazki, zmieniaj biblioteke")
            print("szukkas czy znalazlesz, czy zmienic biblioteke")
            odp = input()

            if odp == "szukam":
                l_test = finder(l_test)
            elif odp == "znalazlem":
                book = book_taker(l_test)
                print("napewno czy jeszcze nie")
                odp = input()

                if odp == "napewno" or odp == 'tak':
                    a = men.test(copy.deepcopy(book))

                    score += a
                    print(f"dostajesz: {a}")
                    f = 1
                elif odp == "nie":
                    pass

            elif odp == "zmienic biblioteke":
                d = 1
                while d != 0:
                    d = 1
                    print(f"masz {len(lb)} bibliotek. W kturej szukasz")
                    odp = input()

                    try:
                        odp = int(odp)
                        d = 0
                    except:
                        print('nope')
                l = lb[odp - 1]
                l_test = finder(l.books)


def sklep():
    global sklep_m, score
    for el in sklep_m:
        if el == "lusterko":
            print(f'llusterko -- 50')
        elif el == "pilka":
            print("pilka -- 10")

    print("Chcesz cos z tego kupic?\n"
          "wprowadz co\n"
          "reszta - wyjsc")
    odp = input()
    if odp == "lusterko":
        if score >= 50:
            print("Kupilesz lusterko")
            sklep_m.remove("lusterko")
            mozliwosci.append("lusterko")
            score -= 50
            print(f"teraz mas {score} punktuw")
        elif score < 50:
            print("brakuje punktuw")
            print(f"teraz mas {score} punktuw")
    elif odp == "pilka":
        if score >= 10:
            print("Kupilesz pilke")
            sklep_m.remove("pilka")
            mozliwosci.append("pilka")
            score -= 10
            print(f"teraz mas {score} punktuw")
        elif score < 10:
            print("brakuje punktuw")
            print(f"teraz mas {score} punktuw")



# def p_nastruj()
#     global nastruj
#     if nastruj < 1:
#         print("nie da sie pracowac")
#     elif 1 <= nastruj < 10:
#         print("masz dypresje")
#     elif 10 <= nastruj <


day_num = 0
score = 0

print("istoria bla bla bla")

end_game = False
day_num = 0
my_lib = Library()
morzliwe_atrakcje = ["posluchac muzyki", 'poczytac ksiazke', "lusterko", "pilka", "spatzer", "gra"]
mozliwosci = ["posluchac muzyki", 'poczytac ksiazke', "gra"]
pogoda = [['sloneicznie', 'spiewaja ptaki'], ['chmurno', 'idzie deszcz']]
# nastruj = 100
sklep_m = ["lusterko", "pilka"]

for f in range(randint(1, 5)):
    my_lib.add_book(Book(choice(name), choice(autor), choice(styl), randint(10, 3000), randint(1900, 2020)))


while end_game != True or day_num < 70:
    day_num += 1
    lb = gen_day()

    pogoda_na_dworze = choice(pogoda)
    if pogoda_na_dworze == pogoda[0]:
        pogoda_na_dworze = choice(pogoda_na_dworze)
        print(pogoda_na_dworze)
        if pogoda_na_dworze == 'spiewaja ptaki':
            pogoda_na_dworze = pogoda[0]
    elif pogoda_na_dworze == pogoda[1]:
        pogoda_na_dworze = choice(pogoda_na_dworze)
        if pogoda_na_dworze == 'idzie deszcz':
            pogoda_na_dworze = pogoda[1]

    print(f"Dzien {day_num}")
    ok = False

    while ok != True:
        print("1 - pujsc pracowac")
        print("2 - pujsc spac")
        print("3 - poszukac czym moge sie zajac")
        if day_num > 7:
            print("4 - pujsc do sklepu")
        wybur = str(input())
        if wybur == '1' or wybur == '2' or wybur == '3' or wybur == '4':
            ok = True
        else:
            print("cos nie tak")
            ok = False

        if wybur == "1":
            praca(lb)
        elif wybur == "2":
            print("ide spac, budze sie nastepnego dnia")
        elif wybur == "3":
            print("Moge:")
            for el in mozliwosci:
                print(el)
            odp = input()

            if odp == "ex":
                pass
            elif odp == "posluchac muzyki":
                s = "sluchas czudowna muzyke "
                if pogoda_na_dworze[0] == 'sloneicznie':
                    s += 'patrzac w okno, jest sloneicznie'
                print(s)
            elif odp == 'poczytac ksiazke':
                print("losowo wybierasz ksiazke")
                print("wybrales:")
                choice(my_lib.books).infb()
            elif odp == "lusterko":
                print('wybierz co stawiasz: "papier kamien norzyce"')
                a = input()
                print("idziesz do lusterka")
                print("papier\n kamien\n norzyce\n")
                print(f"postawilesz {a}, przeciwnik postawil {a}")
                print("remis")
                print("Chyba nigdy nie wygrasz w ta gre...")
            elif odp == "pilka":
                print("Rzucasz pilka w sciane")
                print("wiesolo...")
            elif odp == "spatzer":
                print("Wychodzisz na dwur")
                if len(pogoda_na_dworze) == 2:
                    if pogoda_na_dworze == ['sloneicznie', 'spiewaja ptaki']:
                        print(f"Swieci {choice(['piekne', 'cieple', 'jasne'])}, {pogoda_na_dworze[1]}")
                        print("czujesz sie lepiej")
                    elif pogoda_na_dworze == ['chmurno', 'idzie deszcz']:
                        print(f"ta chmurna pogodoa trafiasz pod deszcz")
                        print("najlepszy dzien na szpacer!")
            elif odp == "gra":
                print("Podchodzisz do komputera i rozpoczynasz gre")
                game()

            ok = False

        elif wybur == "4":
            sklep()
