

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[_______]
*******************************************************************************''')
print("Witaj na niebezpiecznej planecie!")
print("Twoją misją jest przeżyć i zdobyć skarb.")
pierwsza = input("Pierwsza decyzja: Napotykasz wrogo nastawionych lokalnych mieszkańców - uciekasz, czy z nimi porozmawiasz? Napisz - [Porozmawiaj] / [Uciekaj]: ").lower()
while pierwsza != "uciekaj" or "porozmawiaj":
    if pierwsza == "porozmawiaj":
        print("Gratulacje, tutejsi mieszkańcy byli mili i wskazali Ci drogę do upragnionego skarbu :)")
        break
    elif pierwsza == "uciekaj":
        print("Wybrales ucieczke - przegrales.")
        break
    else:
        print("Wybierz odpowiednie słowo z listy")
        pierwsza = input("Pierwsza decyzja: Napotykasz wrogo nastawionych lokalnych mieszkańców - uciekasz, czy z nimi porozmawiasz? Napisz - [Porozmawiaj] / [Uciekaj]: ").lower()
if pierwsza == "porozmawiaj":
    druga = input("Druga decyzja: Idąc do celu strasznie zgłodniałeś i musisz wybrać miejsce, w którym zjesz ciepły posiłek: Wybierz - [KFC] / [Lokalna_Knajpa] ").lower()
    while druga != "kfc" or "lokalna_knajpa":
        if druga == "lokalna_knajpa":
            print("Idealnie! wspierasz lokalne miejsca, lokalni mieszkańcy Cię uwielbiają i oferują Ci podwózke do celu. ")
            break
        elif druga == "kfc":
            print("Niestety za bardzo sie objadles, zasnales i ktos inny zabral skarb")
            break
        else:
            print("Wybierz jeszcze raz z listy")
            druga = input("Druga decyzja: Idąc do celu strasznie zgłodniałeś i musisz wybrać miejsce, w którym zjesz ciepły posiłek: Wybierz - [KFC] / [Lokalna_Knajpa] ").lower()
    if druga == "lokalna_knajpa":
        trzecia = input("Dotarłeś do celu - zawieźli Cię zaprzyjaźnieni mieszkańcy - Jeden z nich naciska, żebyś podzielił się nagrodą i oddał im 20% - Co robisz - [Akceptujesz] / [Odmawiasz] ").lower()
        while trzecia != "akceptujesz" or "odmawiasz":
            if trzecia == "odmawiasz" or "akceptujesz":
                print("Ta decyzja nie miała znaczenia - po prostu chciałem użyć operatora 'OR' żeby w kodzie było więcej funkcjonalności. Gratulacje! :) ")
                break
            else:
                print("Wybierz poprawna opcje")
                trzecia = input("Dotarłeś do celu - zawieźli Cię zaprzyjaźnieni mieszkańcy - Jeden z nich naciska, żebyś podzielił się nagrodą i oddał im 20% - Co robisz - [Akceptujesz] / [Odmawiasz] ").lower()









