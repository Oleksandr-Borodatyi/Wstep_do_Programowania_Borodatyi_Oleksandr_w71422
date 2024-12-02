#Zadanie 3

# Wczytanie liczby naturalnej n oraz dwóch liczb rzeczywistych a i r
n = int(input("Podaj liczbę naturalną n: "))
a = float(input("Podaj pierwszy wyraz ciągu a: "))
r = float(input("Podaj różnicę r: "))

# Wypisanie n elementów ciągu arytmetycznego
print("Elementy ciągu arytmetycznego:")
for i in range(n):
    element = a + i * r  # Wzór na n'ty element ciągu arytmetycznego
    print(element)