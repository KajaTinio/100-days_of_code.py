#ROCK PAPER SCISSORS
import random
gracz = int(input("Co wybierasz? Kamień: [0], Papier[1], czy Nożyce [2]: "))
lista = ["Kamień", "Papier", "Nożyce"]
komputer = int(random.randint(0,2))
print(f"Wybrałeś:{gracz}")
print(f"Komputer wybrał: {komputer}")
if gracz >= 3 or komputer < 0:
    print("Podaj liczbe z zakresu 0-2, Przegrałeś")
elif gracz == 0 and komputer == 2:
    print("Wygrałeś!")
elif gracz == 2 and komputer == 0:
    print("Przegrałeś :C ")
elif gracz > komputer:
    print("Wygrałeś!")
elif gracz == komputer:
    print("Remis")









