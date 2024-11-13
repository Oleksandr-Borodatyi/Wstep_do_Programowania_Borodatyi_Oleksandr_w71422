# Pobranie współczynników od użytkownika
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))

# Sprawdzenie wartości współczynnika a
if a == 0:
    if b == 0:
        print("Równanie ma nieskończenie wiele rozwiązań.")
    else:
        print("Równanie jest sprzeczne i nie ma rozwiązań.")
else:
    # Obliczenie wyniku
    x = -b / a
    print("Rozwiązaniem równania jest x =", x)
