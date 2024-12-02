#Zadanie 7

import random

# Tworzenie zbiorów X i Y z losową liczbą elementów
a = random.randint(3, 7)  # Losowa liczba elementów dla X
b = random.randint(3, 7)  # Losowa liczba elementów dla Y
X = set(random.randint(0, 10) for _ in range(a))
Y = set(random.randint(0, 10) for _ in range(b))

print("Zbiór X:", X)
print("Zbiór Y:", Y)

# a) Czy X zawiera liczbę 5
print("Czy zbiór X zawiera liczbę 5?:", 5 in X)

# b) Czy X jest podzbiorem Y
print("Czy zbiór X jest podzbiorem zbioru Y?:", X.issubset(Y))

# c) Czy Y jest podzbiorem X
print("Czy zbiór Y jest podzbiorem zbioru X?:", Y.issubset(X))

# d) Suma zbiorów X i Y
print("Suma zbiorów X i Y:", X | Y)

# e) Różnica zbiorów X i Y
print("Różnica zbiorów X i Y:", X - Y)

# f) Różnica zbiorów Y i X
print("Różnica zbiorów Y i X:", Y - X)

# g) Iloczyn zbiorów X i Y
print("Iloczyn zbiorów X i Y:", X & Y)

# h) Najwyższy element w obu zbiorach
max_element = max(X | Y) if X or Y else None  # Sprawdzamy, czy zbiory nie są puste
print("Najwyższy element w obu zbiorach:", max_element)

# i) Usuń pierwszy element z X i dołącz go do Y
if X:
    pierwszy_element = next(iter(X))  # Pobieramy pierwszy element
    X.remove(pierwszy_element)  # Usuwamy go z X
    Y.add(pierwszy_element)  # Dodajemy go do Y
    print("Po przeniesieniu pierwszego elementu:")
    print("Zbiór X:", X)
    print("Zbiór Y:", Y)

# j) Przekopiuj wszystkie elementy z X do Y
Y.update(X)
print("Po przekopiowaniu elementów z X do Y:")
print("Zbiór Y:", Y)

# k) Wyczyść oba zbiory
X.clear()
Y.clear()
print("Po wyczyszczeniu zbiorów:")
print("Zbiór X:", X)
print("Zbiór Y:", Y)
