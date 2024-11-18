#Zadanie 3

# Wczytanie ciągu znaków od użytkownika
ciag = input("Podaj ciąg znaków: ")

# Usunięcie spacji i zamiana na małe litery, aby ignorować wielkość liter i białe znaki
ciag_czysty = ''.join(znak.lower() for znak in ciag if znak.isalnum())

# Sprawdzenie, czy ciąg jest palindromem
if ciag_czysty == ciag_czysty[::-1]:
    print("Tak, podany ciąg jest palindromem.")
else:
    print("Nie, podany ciąg nie jest palindromem.")
