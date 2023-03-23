# temperature = float(input("pomiar temp"))
# if temperature < 28 or temperature > 41:
#     print("zagrozenie zycia")
# else:
#     print("Temp "+str(temperature))
#
# pressure = (input("pomiar cisnienia"))
# symptoms = (input("objawy"))
# if pressure == "180/110" and symptoms == "bol klaty":
#     print("zagrozenie zycia")
# else:
#     print("jest gituwa")

# while True:
#     dane = input("podaj dane (end - konczy): ")
#     if dane == "end":
#         break
#     print(dane)
#
# i = 0
# while i < 10:
#     i += 1
#     print(i)

# i = 0
# while i < 10:
#
#     if i == 5:
#         i += 1
#         continue
#     print(i)
#     i += 1

# for i in (range(0, 10)):
#     print(i)
#
# #printuje co 2
# for i in (range(0, 10, 2)):
#     print(i)

# cityList = ["Warszawa", "Krakow", "Wroclaw", "Lodz", "Poznan",
#             "Gdansk", "Szczecin", "Bydgoszcz", "Lublin", "Bialystok"]
# print(cityList)
#
# for index in range(0, len(cityList)):
#     print(cityList[index])
#
# for element in cityList:
#     print(element)
#
# for index in range(0, len(cityList)):
#     cityList[index] = "brak danych"
# print(cityList)
#
# cityList = ["Warszawa", "Krakow", "Wroclaw", "Lodz", "Poznan",
#             "Gdansk", "Szczecin", "Bydgoszcz", "Lublin", "Bialystok"]
#
# cityList.append("Walbrzych")
# print(cityList)
#
# cityList.insert(0, "Walbrzych")
# print(cityList)
#
# cityList.extend(["nowa", "nowa"])
# print(cityList)
#
# del cityList[0]
# print(cityList)
#
# print(cityList.pop())
# print(cityList.pop(0))
# print(cityList)
#
# index = cityList.index("nowa")
# print(index)
# print(cityList.pop(index))
# print(cityList[-1])
# cityList.insert(0, "Warszawa")
#
# miasto = "radom"
# if miasto in cityList:
#     cityList.remove(miasto)
# else:
#     print("nie ma")
#
# cityList.insert(5, "nowa")
# cityList.insert(2, "nowa")
# print(cityList)
# miasto = "nowa"
#
# while miasto in cityList:
#     cityList.remove(miasto)
# print(cityList)
#
# print(max(cityList))
#
# liczby = list(range(0,10))
# print(sum(liczby))
# print(max(liczby))
# print(min(liczby))
#
# dane = "4,5,6,7,8"
# lista = dane.split(",")
# print(lista)

import random
import sys
from getpass import getpass

#Zad 1
#----------------------------------------------------------------------------------------------
print(sys.executable)
minmaxy = input("Podaj liczby po przecinku by wyznaczyc ktora jest najmniejsza albo najwieksza")
cyferki = minmaxy.split(",")
print(cyferki)

mini = cyferki[0]
maxi = cyferki[0]

for i in range(1, len(cyferki)):
    if cyferki[i] > maxi:
        maxi = cyferki[i]
    elif cyferki[i] < mini:
        mini = cyferki[i]
print("Minimalna: "+str(mini)+" Maksymalna: "+str(maxi))

#Zad 2
#----------------------------------------------------------------------------------------------

miasta = ["Warszawa", "Krakow", "Wroclaw", "Lodz", "Poznan",
            "Gdansk", "Szczecin", "Bydgoszcz", "Lublin", "Bialystok"]
odwiedzoneMiasta = []

wylosowane = ""
while len(odwiedzoneMiasta) < len(miasta):
    wylosowane = random.choice(miasta)
    if wylosowane not in odwiedzoneMiasta:
        odwiedzoneMiasta.append(wylosowane)
print(odwiedzoneMiasta)

#Zad 3 (dziala w terminalu ale nie w runie)
#----------------------------------------------------------------------------------------------

gameMode = input("Wybierz tryb gry: 'K' - gracz vs komputer, 'G' - gracz vs gracz (hot seats)")
turns = int(input("Do ilu zwyciestw chcesz zagrac?"))

wybory = ["papier", "kamien", "nozyce"]

player1 = 0
player2 = 0
playerK = 0

p1input = ""
p2input = ""
pKinput = ""
if gameMode == "K":
    while player1 < turns and playerK < turns:
        p1input = input("Co wyrzucasz? 'papier', 'kamien', 'nozyce'?")
        pKinput = random.choice(wybory)
        print(pKinput)

        if p1input == "papier" and pKinput == "kamien":
            player1 += 1
            print("Gracz 1: " + str(player1) + " Komputer: " + str(playerK))
        elif p1input == "papier" and pKinput == "nozyce":
            playerK += 1
            print("Gracz 1: " + str(player1) + " Komputer: " + str(playerK))
        elif p1input == "kamien" and pKinput == "papier":
            playerK += 1
            print("Gracz 1: " + str(player1) + " Komputer: " + str(playerK))
        elif p1input == "kamien" and pKinput == "nozyce":
            player1 += 1
            print("Gracz 1: " + str(player1) + " Komputer: " + str(playerK))
        elif p1input == "nozyce" and pKinput == "kamien":
            playerK += 1
            print("Gracz 1: " + str(player1) + " Komputer: " + str(playerK))
        elif p1input == "nozyce" and pKinput == "papier":
            player1 += 1
            print("Gracz 1: " + str(player1) + " Komputer: " + str(playerK))
        else:
            print("Remis!!! Gracz 1: " + str(player1) + " Komputer: " + str(playerK))
elif gameMode == "G":
    while player1 < turns and player2 < turns:
        print("Gracz 1: co wyrzucasz? 'papier', 'kamien', 'nozyce'?")
        p1input = getpass("")
        print("Gracz 2: co wyrzucasz? 'papier', 'kamien', 'nozyce'?")
        p2input = getpass("")
        print("Gracz 1 wybral:", p1input, "Gracz 2 wybral:", p2input)

        if p1input == "papier" and pKinput == "kamien":
            player1 += 1
            print("Gracz 1: " + str(player1) + " Gracz 2: " + str(player2))
        elif p1input == "papier" and p2input == "nozyce":
            player2 += 1
            print("Gracz 1: " + str(player1) + " Gracz 2: " + str(player2))
        elif p1input == "kamien" and p2input == "papier":
            player2 += 1
            print("Gracz 1: " + str(player1) + " Gracz 2: " + str(player2))
        elif p1input == "kamien" and p2input == "nozyce":
            player1 += 1
            print("Gracz 1: " + str(player1) + " Gracz 2: " + str(player2))
        elif p1input == "nozyce" and p2input == "kamien":
            player2 += 1
            print("Gracz 1: " + str(player1) + " Gracz 2: " + str(player2))
        elif p1input == "nozyce" and p2input == "papier":
            player1 += 1
            print("Gracz 1: " + str(player1) + " Gracz 2: " + str(player2))
        else:
            print("Remis!!! Gracz 1: " + str(player1) + " Gracz 2: " + str(player2))
else:
    print("wybrano nieznany tryb")