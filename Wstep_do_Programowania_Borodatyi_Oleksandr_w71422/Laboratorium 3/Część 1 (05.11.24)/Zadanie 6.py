#Zadanie 6 

# Zdefiniowanie słownika z rachunkami za prąd (klucz: miesiąc, wartość: rachunek)
rachunki = {
    "Styczeń": 220,
    "Luty": 180,
    "Marzec": 200,
    "Kwiecień": 210,
    "Maj": 190,
    "Czerwiec": 230
}

# a) Wyznaczanie wartości maksymalnej, minimalnej, sumy oraz średniej
maksymalna_wartosc = max(rachunki.values())
minimalna_wartosc = min(rachunki.values())
suma_wartosci = sum(rachunki.values())
srednia_wartosc = suma_wartosci / len(rachunki)

print("Maksymalna wartość:", maksymalna_wartosc)
print("Minimalna wartość:", minimalna_wartosc)
print("Suma wartości:", suma_wartosci)
print("Średnia wartość:", round(srednia_wartosc, 2))

# b) Sprawdzanie wartości ostatniego miesiąca
ostatni_miesiac = list(rachunki.keys())[-1]
ostatnia_wartosc = rachunki[ostatni_miesiac]

if ostatnia_wartosc > srednia_wartosc:
    print("Trzeba zacisnąć pasa")
else:
    print("Wszystko okay")
