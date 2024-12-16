# Zadanie 10 

import random
import math

def oblicz_srednia_geometryczna(krotka):
    """
    Funkcja oblicza średnią geometryczną dla danej krotki.
    Średnia geometryczna to n-ta pierwiastek z iloczynu n liczb.
    """
    iloczyn = math.prod(krotka)  
    return iloczyn ** (1 / len(krotka))  

min_value = int(input("Podaj minimalną wartość przedziału: "))
max_value = int(input("Podaj maksymalną wartość przedziału: "))

krotka = tuple(random.randint(min_value, max_value) for _ in range(10))

print("Wylosowana krotka:", krotka)

srednia_geometryczna = oblicz_srednia_geometryczna(krotka)
print("Średnia geometryczna krotki wynosi:", srednia_geometryczna)
