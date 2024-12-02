# Zadanie 6

def wypisz_imie_i_wiek(imie, wiek=20):
    """
    Funkcja wypisuje na ekranie podane imię i wiek.
    Jeśli wiek nie zostanie podany, funkcja używa wartości domyślnej 20.
    """
    print(f"Imię: {imie}, Wiek: {wiek}")

print(wypisz_imie_i_wiek.__doc__)

wypisz_imie_i_wiek("Jan", 25)  
wypisz_imie_i_wiek("Anna")     
