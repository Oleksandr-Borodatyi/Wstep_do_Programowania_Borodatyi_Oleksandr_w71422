#Zadanie 2
import string

# Wczytanie zdania od użytkownika
zdanie = input("Podaj zdanie: ")

# a) Litery w kolejności alfabetycznej i brakujące litery
litery_w_zdaniu = sorted(set(filter(str.isalpha, zdanie.lower())))
alfabet = set(string.ascii_lowercase)
brakujace_litery = alfabet - set(litery_w_zdaniu)

print("Litery w zdaniu w kolejności alfabetycznej:", ''.join(litery_w_zdaniu))
print("Litery, których brakuje w zdaniu:", ''.join(sorted(brakujace_litery)))

# b) Usunięcie znaków o nieparzystych indeksach
pozostale_znaki = zdanie[::2]
print("Zdanie po usunięciu znaków o nieparzystych indeksach:", pozostale_znaki)

# c) Każdy wyraz zaczyna się i kończy wielką literą
wyrazy = zdanie.split()
wyrazy_wielkie = [wyraz.capitalize()[:-1] + wyraz[-1].upper() if len(wyraz) > 1 else wyraz.upper() for wyraz in wyrazy]
zdanie_wielkie = ' '.join(wyrazy_wielkie)
print("Zdanie, gdzie każdy wyraz zaczyna się i kończy wielką literą:", zdanie_wielkie)

# d) Najdłuższe słowo i jego długość
najdluzsze_slowo = max(wyrazy, key=len, default="")
print("Najdłuższe słowo:", najdluzsze_slowo)
print("Długość najdłuższego słowa:", len(najdluzsze_slowo))

# e) Zamiana powtarzających się znaków na @
wynik = []
wystapienia = set()
for znak in zdanie:
    if znak in wystapienia:
        wynik.append('@')
    else:
        wynik.append(znak)
        wystapienia.add(znak)

zmieniony_ciag = ''.join(wynik)
print("Ciąg z powtarzającymi się znakami zamienionymi na @:", zmieniony_ciag)
