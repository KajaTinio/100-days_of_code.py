#HANGMAN
import random
lista_slow = ["jabłko", "pies", "kot", "gruszka"]
liczba_prob = ["Pozostało Ci 8 żyć"]

dostepne_zycia = 8
wybrane_slowo = random.choice(lista_slow)

koniec_gry = False
odgadniete_litery = []
while not koniec_gry:

    proba = input("Wybierz jedną literę: ").lower()
    dlugosc_slowa = len(wybrane_slowo)


    ekran = ""

    for litera in wybrane_slowo:
        if litera == proba:
            ekran += litera
            odgadniete_litery.append(proba)
        elif litera in odgadniete_litery:
            ekran += litera
        else:
            ekran += "_"

    print(ekran)


    if "_" not in ekran:
        koniec_gry = True
        print("Wygrałeś!")

    if proba not in odgadniete_litery:
        dostepne_zycia -= 1
        if dostepne_zycia == 0:
            koniec_gry = True

    if proba == wybrane_slowo:
        koniec_gry = True

        print("Gratulacje, wygrałeś!")

    print(f"Pozostało Ci: {dostepne_zycia} ❤️")












