# Zadanie 10

import string

# Tworzenie listy wszystkich liter alfabetu
alfabet = list(string.ascii_lowercase)

# Pobranie wartości n od użytkownika
n = int(input("Podaj wartość n: "))

# Sprawdzenie, czy n jest większe niż 0
if n <= 0:
    print("Wartość n musi być większa od 0.")
else:
    # Podzielenie listy na podlisty co n elementów
    podlisty = [alfabet[i:i + n] for i in range(0, len(alfabet), n)]

    # Wyświetlenie wynikowej listy
    print(podlisty)
