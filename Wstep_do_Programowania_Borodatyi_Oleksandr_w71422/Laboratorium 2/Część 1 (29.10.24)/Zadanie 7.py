#Zadanie 7

# a) Wczytanie imienia
imie = input("Podaj swoje imię: ")
print("Witaj", imie)


# b) Wczytanie wieku
wiek = int(input("Podaj swój wiek: "))
print("Twój wiek to:", wiek)


# c) Wczytanie imienia i nazwiska
imie_nazwisko = input("Podaj swoje imię i nazwisko: ")
imie, nazwisko = imie_nazwisko.split()  # Rozdzielenie imienia i nazwiska
inicjaly = imie[0].upper() + nazwisko[0].upper()  # Inicjały
print("Twoje inicjały to:", inicjaly)


# d) Wczytanie łańcucha
lancuch = input("Podaj łańcuch tekstowy: ")
print("Twój łańcuch pięć razy:")
print(lancuch * 5)  # Powielanie łańcucha pięć razy


# e) Wczytanie dwóch łańcuchów
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
polaczony_lancuch = lancuch1 + lancuch2  # Połączenie łańcuchów
print("Połączony łańcuch:", polaczony_lancuch)


# f) Wczytanie dwóch łańcuchów
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")


# Obliczanie połowy długości
polowa1 = len(lancuch1) // 2  # Pierwsza połowa pierwszego łańcucha
polowa2 = len(lancuch2) // 2  # Druga połowa drugiego łańcucha


# Tworzenie nowego łańcucha
nowy_lancuch = lancuch1[:polowa1] + lancuch2[polowa2:]  # Połączenie

print("Nowy łańcuch:", nowy_lancuch)
