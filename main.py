import random
import string
from itertools import count
from operator import index

# # kintamieji
# # uzduotis 1
# vardas = 'Jenna'
# pavard = 'Ortega'
# result = vardas + ' ' + pavard
# print(result)

# uzduotis 2

# vardas = 'Jenna'
# vardas = vardas.upper()
# pavard = 'Ortega'
# pavard = pavard.lower()
# result = vardas + ' ' + pavard
# print(result)
#
# # uzduotis 3
# vardas = 'Jenna'
# pavard = 'Ortega'
# three = vardas[:3] + pavard[:3]
# print(three)

# # uzduotis 4

# vardas = 'Jenna'
# pavard = 'Ortega'
# three = vardas[-3:] + pavard[-3:]
# print(three)

# # uzduotis 5

# filmas = 'An American in Paris'
# naujas = filmas.replace('A', '*')
# naujas2 = naujas.replace('a', '*')
# print(naujas2)

# # uzduotis 6

# filmas = 'An American in Paris'
# print(filmas.translate({ord(i): None for i in 'AaEeIiOoUuYy'}))
# filmas2 = "Breakfast at Tiffany's"
# print(filmas2.translate({ord(i): None for i in 'AaEeIiOoUuYy'}))
# filmas3 = "2001: A Space Odyssey"
# print(filmas3.translate({ord(i): None for i in 'AaEeIiOoUuYy'}))
# filmas4 = "It's a Wonderful Life"
# print(filmas4.translate({ord(i): None for i in 'AaEeIiOoUuYy'}))
#

# uzduotis 7

# starWars = "Star Wars: Episode " + ("" * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# print(starWars)
# print(starWars[19])
#
#
# uzduotis 8

# filmas = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
# raides = list(map(len, filmas.split()))
# print(raides)
# print(raides.count(5) + raides.count(4) + raides.count(3) + raides.count(2) + raides.count(1))
# filmas2 = "Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale"
# raides2 = list(map(len, filmas2.split()))
# print(raides2)
# print(raides2.count(5) + raides2.count(4) + raides2.count(3) + raides2.count(2) + raides2.count(1))

# uzduotis 9

# pirmas = random.choice(string.ascii_lowercase)
# antras = random.choice(string.ascii_lowercase)
# trecias = random.choice(string.ascii_lowercase)
# print(pirmas + antras + trecias)

# uzduotis 10

# filmas = ["Don't", "Be", "a", "Menace", "to", "South", "Central", "While", "Drinking", "Your", "Juice", "in", "the", "Hood"]
# filmas2 = ["Tik", "nereikia", "gąsdinti", "Pietų Centro,", "geriant", "sultis", "pas", "save", "kvartale"]
# vienas = random.sample(filmas, 5)
# antras = random.sample(filmas2, 5)
# eilute = vienas + antras
# print(' '.join(eilute))
#

# sarasai
# uzduotis 1
#
# vardai = ['Monika', 'Naglis', 'Miksas', 'Pupa']
# print(' '.join(vardai))
# print('vardu kiekis:', len(vardai))
# print('pirmas vardas:', vardai[0])
# print('paskutinis vardas:', vardai[len(vardai) - 1])

# uzduotis 2

# ugiai = ['200 cm', '187 cm', '165 cm', '150 cm', '190 cm', '155 cm', '172 cm']
# print(' '.join(ugiai))
# print('ugiu kiekis:', len(ugiai))

# uzduotis 3

# pazymiai = [8, 7, 9, 9, 8]
# print(pazymiai)
# while True:
#     user_input = input("Ar norite ivesti daugiau pazymiu? (taip/ne): ")
#     if user_input.lower() in ["taip", "t"]:
#         print("Iveskite pazymi:")
#         naujas = int(input())
#         pazymiai.append(naujas)
#     elif user_input.lower() in ["ne", "n"]:
#         average = round(sum(pazymiai) / len(pazymiai), 2)
#         print("Visi pazymiai:", pazymiai)
#         print('Pazymiu vidurkis:', average)
#         break
#     else:
#         print("Neteisingas pasirinkimas, irasykite TAIP arba NE")

# uzduotis 4

# miestai = ['Vilnius', 'Kaunas', 'Klaipeda']
# miestai.append('Marijampole')
# miestai.extend(['Sakiai', 'Jurbarkas'])
# print(miestai)
# print("Iveskite miesta:")
# naujas = input()
# miestai.append(naujas)
# print(miestai)
# print("Iveskite miesta:")
# naujas2 = input()
# print('Iveskite pozicijos numeri kur prideti irasyta miesta i sarasa:')
# pozicija = int(input())
# miestai.insert(pozicija - 1, naujas2)
# print(miestai)

# uzduotis 5

# salys = []
# salys.extend(['Lietuva', 'Latvija', 'Estija', 'USA', 'Peru'])
# salys.append('Norvegija')
# print(salys)
# salys.pop()
# salys.pop()
# print(salys)
# print('Irasykite skaiciu kiek dar pasalinti duomenu:')
# skaicius = int(input())
# del salys[0:skaicius]
# print(salys)

# uzduotis 6

# salys = ['Lietuva', 'Latvija', 'Estija', 'USA', 'Peru', 'Norvegija']
# print(salys)
# if len(salys) > 5:
#     salys.clear()
#     print(salys)
# else:
#     print(salys)
#
# uzduotis 7

# zodziai = ['Lietuva', 'Latvija', 'Estija', 'USA', 'Peru', 'Norvegija', 'Geles', 'Vartai', 'Mokykla']
# print("Iveskite zodi paieskai:")
# naujas = input()
# try:
#     print('Zodis sarase uzima', zodziai.index(naujas) + 1, 'vieta')
# except ValueError:
#     print("That item does not exist")

# uzduotis 8

# pazymiai = [8, 7, 9, 9, 8, 10, 8, 10]
# print(pazymiai)
# while True:
#     user_input = input("Ar norite ivesti daugiau pazymiu? (taip/ne): ")
#     if user_input.lower() in ["taip", "t"]:
#         print("Iveskite pazymi:")
#         naujas = int(input())
#         pazymiai.append(naujas)
#     elif user_input.lower() in ["ne", "n"]:
#         kiekis = pazymiai.count(10)
#         print("Visi pazymiai:", pazymiai)
#         print('Desimtuku kiekis:', kiekis)
#         break
#     else:
#         print("Neteisingas pasirinkimas, irasykite TAIP arba NE")

# uzduotis 9
#
# auto = ['Audi', 'BMW', 'Subaru', 'Wolksvagen', 'Kia', 'Citroen', 'Nissan']
# print(auto)
# auto.sort()
# print(auto)
# auto.reverse()
# print(auto)

# uzduotis 10
# pazymiai = []
# pazymiai.extend([8, 7, 9, 9, 8, 10, 8, 10])
# print(pazymiai)
# pazymiai.sort(reverse=True)
# print('Trys didziausi pazymiai:', pazymiai[0], pazymiai[1], pazymiai[2])

# uzuotis 11

# pazymiai = []
# pazymiai.extend([8, 7, 9, 9, 8, 10, 8, 10, 4, 3, 10, 2, 1])
# print(pazymiai)
# if 1 or 2 or 3 or 4 in pazymiai:
#     print('Mokinys turi', pazymiai.count(1) + pazymiai.count(2) + pazymiai.count(3) + pazymiai.count(4), 'neigiamus pazymius')
# else:
#     print("Neigiamu pazymiu nera")

# uzduotis 12

# pazymiai = [8, 7, 9, 9, 8, 10, 8, 10, 4, 3, 10, 2, 1]
# print(pazymiai)
# print(pazymiai[0:3])
# print(pazymiai[3:5])
# print(pazymiai[-4:])
# print(pazymiai[2:14:2])
# pazymiai.sort(reverse=True)
# print(pazymiai)

# uzduotis 13

# vidurkiai = ['8.5', '9', '8.3', '7.5', '8', '9.1', '6.6', '7.2']
# print(vidurkiai)
# vidurkiai.sort(reverse=True)
# print(vidurkiai)
# maxtrys = [vidurkiai[0], vidurkiai[1], vidurkiai[2]]
# print(maxtrys)

# uzduotis 14

# zodynas = ['lape', 'katinas', 'medis']
# zodynas.sort()
# print(zodynas)
# while True:
#     user_input = input("Ar norite ivesti daugiau duomenu? (taip/ne): ")
#     if user_input.lower() in ["taip", "t"]:
#         print('Iveskite nauja zodi:')
#         naujas = input()
#         zodynas.append(naujas)
#         zodynas.sort()
#         print(zodynas)
#     elif user_input.lower() in ["ne", "n"]:
#         zodynas.sort()
#         print(zodynas)
#         break
#     else:
#         print(zodynas)

# uzduotis 15

# likuciai = []
# likuciai.append(['Dviraciai', 20])
# likuciai.append(['Batai', 30])
# likuciai.append(['Kojines', 10])
# print(likuciai)

# uzduotis 16

# listas = []
# listas.extend(['Lietuva', 'Latvija', 'Estija', 'USA', 'Peru', 'Norvegija', 'Geles', 'Vartai', 'Mokykla'])
# print(', '.join(listas))
# print('|'.join(listas))
# print(' '.join(listas))

# uzduotis 17

# a, b, *other = ['Python', 'Desktop', 'Project1', 'Project2', 'Project3']
# print('Naudojama programavimo kalba:', a)
# print('Dirbama su:', b)
# print('Projektu pavadinimai:', other)

# ciklai
# uzduotis 1
#
# for var in range(5):
#     print('Monika')

# Uzduotis 2

# kiekis = 11
# for i in range(kiekis):
#     print(i)

# uzduotis 3

# kiekis = 16
# for i in range(kiekis):
#     if i % 2 == 0:
#         continue
#     print(i)

# uzduotis 4

# for i in range(0, 21, 3):
#     print(f'[{i}]')

# uzduotis 5

# kiekis = 21
# for i in range(kiekis):
#     if i % 4 == 0:
#         print(i)

# uzduotis 6

# for i in range(1, 16):
#     if i % 2 == 0:
#         print(i, 'yra lyginis')
#     else:
#         print(i, 'yra nelyginis')

# uzduotis 7

# pradzia, pabaiga = 5, 30
# if pradzia < pabaiga:
#     for i in range(pradzia, pabaiga + 1):
#         print(i, i*i)

# uzduotis 8
#
# pradzia, pabaiga = 5, 30
# if pradzia < pabaiga:
#     for i in range(pradzia, pabaiga + 1):
#         if i % 2 == 1 or i % 8 == 0:
#             print(i, 'yra nelyginis arba dalinasi is 8')

# uzduotis 9

# print('Iveskite savo varda')
# naujas = input()
# for i in range(len(naujas)):
#     print('Labas', naujas)

# uzduotis 10

# for i in [88, 65, 21, 26, 47]:
#     if i % 2 == 0:
#         print(i)

# uzduotis 11
#
# print('Iveskite reziu pradzia:')
# pradzia = int(input())
# print('Iveskite reziu pabaiga:')
# pabaiga = int(input())
# print('Iveskite norima zingsni (skaiciais)')
# zingsnis = int(input())
# print('Irasykite norite matyti lyginius ar nelyginius skaicius (rasyti l arba n)')
# arlyg = input()
# print(pradzia, pabaiga, zingsnis)
# if pradzia < pabaiga:
#     for i in range(pradzia, pabaiga, zingsnis):
#             if arlyg in 'l':
#                  if i % 2 == 0:
#                     print(i)
#             else:
#                 if i % 2 == 1:
#                     print(i)

# uzduotis 12
#
# simb = '*'
# print("iveskite eiluciu kieki:")
# skaicius = int(input())
# for i in range(0, skaicius + 1):
#     print(simb * i)
#

# uzduotis 13

# print("Iveskite zodi:")
# zodis = input()

# uzduotis 14

# print("iveskite pirma skaiciu:")
# skaicius = int(input())
# print("iveskite antra skaiciu:")
# skaicius2 = int(input())
#
# def multiply(x, y):
#     if y < 0:
#         return -multiply(x, -y)
#     elif y == 0:
#         return 0
#     elif y == 1:
#         return x
#     else:
#         return x + multiply(x, y - 1)
#
# print('Ivestu skaiciu sandauga:')
# print(multiply(skaicius, skaicius2))

# uzduotis 15

# suma = 0
# for i in range(100):
#     suma += i
# print(f'gauta suma: {suma}')


# uzduotis 16
#
# suma = 0
# for i in range(20,50):
#     if i % 2 == 0:
#         suma += i
# print(f'lyginiu nuo 20 iki 50 suma: {suma}')

# uzduotis 17

# suma = 0
# for i in range(30,60):
#     if i % 2 == 1:
#         suma += i
# print(f'nelyginiu nuo 30 iki 60 suma: {suma}')

# uzduotis 18

# suma = 0
# sarasas = []
# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         sarasas.append(i)
#         suma += i
# print(f'Visi skaičiai mažesni už 1000 ir kurie dalinasi iš 3 arba 5 yra: {sarasas}')
# print(f'skaiciu suma yra: {suma}')


# --------------------------------------
# ciklai 2
# 3 uzduotis
#
# augalai = ['roze', 'tulpe', 'azuolas', 'pluke', 'lelija', 'berzas', 'uosis', 'egle', 'dilgele', 'liepa']
# print(', '.join(augalai))

# 4 uzduotis
#
# index = 0
#
# while index < len(augalai):
#     print(augalai[index])
#     index += 1
#
# # 5 uzduotis
#
# index = 9
#
# while index < len(augalai) + 1:
#     print(augalai[index])
#     index -= 1
#     if index == 0:
#         break

# -------------------------------------------------------------------
# ciklas while

# Uzduotis 1

# skaicius = 1
# while skaicius < 21:
#     print(skaicius)
#     skaicius += 1

# Uzduotis 2

# skaicius = 1
# while skaicius < 51:
#     if skaicius % 2 == 0:
#         print(skaicius, 'lyginis')
#         skaicius += 1
#     else:
#         print(skaicius, 'nelyginis')
#         skaicius += 1

# Uzduotis 3

# skaicius = 25
# while skaicius < 51:
#     if skaicius % 3 == 0:
#         print('dalinasi is 3')
#         skaicius += 1
#     else:
#         print(skaicius)
#         skaicius += 1

# Uzduotis 4

# skaicius = 1
# while skaicius < 100:
#     print(skaicius)
#     skaicius += 1
#     if skaicius == 7:
#         break

# Uzduotis 5

# skaicius = 1
# while skaicius < 1000:
#     print(skaicius)
#     skaicius += 1
#     if skaicius % 3 == 0 and skaicius % 5 == 0:
#         break

# Uzduotis 6

# print('Iveskite reziu pradzia:')
# pradzia = int(input())
# print('Iveskite reziu pabaiga:')
# pabaiga = int(input())
# if pradzia > pabaiga:
#     print('Klaida, neteisingi reziai, pradzia turi buti mazesne uz pabaiga! Iveskite is naujo.')
#     print('Iveskite reziu pradzia:')
#     pradzia = int(input())
#     print('Iveskite reziu pabaiga:')
#     pabaiga = int(input())
#     while pradzia < pabaiga:
#         continue
# for i in range(pradzia, pabaiga + 1):
#     if i % 2 == 0:
#         lyg = 'Lyginis'
#     else:
#         lyg = 'Nelyginis'
#     print(f'{i} {lyg}, skaiciaus kvadratas: {i * i}')

# uzduotis 7

# primes = []
# for possiblePrime in range(1, 30):
#     # Assume number is prime until shown it is not.
#     isPrime = True
#     for num in range(2, possiblePrime):
#         if possiblePrime % num == 0:
#             isPrime = False
#     if isPrime:
#         primes.append(possiblePrime)
#         if possiblePrime > 20:
#             break
# print(primes)

# uzduotis 8

# skaiciai = []
# while True:
#     print('Iveskite betkoki skaiciu:')
#     sk = int(input())
#     skaiciai.append(sk)
#     if sk == 0:
#         break
# print('Ivestu skaiciu suma:', sum(skaiciai))

# uzduotis 9
while True:
    print('Iveskite pirma skaiciu:')
    sk = int(input())
    print('Iveskite antra skaiciu:')
    sk2 = int(input())
    print('Irasykite norima veiksma - sudetis, atimtis, daugyba ar dalyba:')
    veiksmas = input()
    if veiksmas == 'sudetis':
        print(sk, '+', sk2, '=', sk + sk2)
    if veiksmas == 'atimtis':
        print(sk, '-', sk2, '=', sk - sk2)
    if veiksmas == 'daugyba':
        print(sk, '*', sk2, '=', sk * sk2)
    if veiksmas == 'dalyba':
        print(sk, '/', sk2, '=', sk / sk2)
    user_input = input('Ar norite pakartoti is naujo? (taip/ne): ')
    if user_input.lower() in ["taip", "t"]:
        continue
    elif user_input.lower() in ["ne", "n"]:
        break



#   while True:
# #     user_input = input("Ar norite ivesti daugiau pazymiu? (taip/ne): ")
# #     if user_input.lower() in ["taip", "t"]:
# #         print("Iveskite pazymi:")
# #         naujas = int(input())
# #         pazymiai.append(naujas)
# #     elif user_input.lower() in ["ne", "n"]:
# #         average = round(sum(pazymiai) / len(pazymiai), 2)
# #         print("Visi pazymiai:", pazymiai)
# #         print('Pazymiu vidurkis:', average)
# #         break
# #     else:
# #         print("Neteisingas pasirinkimas, irasykite TAIP arba NE")