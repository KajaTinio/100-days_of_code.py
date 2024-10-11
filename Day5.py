#PASSWORD GENERATOR
import random
litery_lista = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "o", "ó", "p", "q", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż"]
liczby_lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "13", "14", "15", "16", "17", "18", "19", "20","21", "22", "23", "24", "25", "26", "27", "28", "29", "30","31", "32"]
symbole_lista = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "\"", "<", ">", ",", ".", "?", "/", "\\", "|", "~", "`"]

print("Witaj w generatorze haseł!")
litery = int(input("Ile chciałbyś mieć liter w swoim haśle: "))
liczby = int(input("Ile chciałbyś mieć znaków w swoim haśle: "))
symbole = int(input("Ile chciałbyś mieć liczb w swoim haśle: "))

lista_hasla = []
for znak in range (0, litery):
        lista_hasla.append(random.choice(litery_lista))

for znak in range(0, liczby):
        lista_hasla.append(random.choice(liczby_lista))

for znak in range(0, symbole):
        lista_hasla.append(random.choice(symbole_lista))


random.shuffle(lista_hasla)


haslo = ""
for znak in lista_hasla:
        haslo += znak
print("Twoje hasło:", haslo)















