# Zadanie 11

import random

def sprawdz_liczbe(x):
    try:
        return int(x)
    except ValueError:
        return None

def zgadnij_liczbe():
    while True:
        zakres_min = input("Podaj minimalną wartość zakresu: ")
        zakres_max = input("Podaj maksymalną wartość zakresu: ")
        
        zakres_min = sprawdz_liczbe(zakres_min)
        zakres_max = sprawdz_liczbe(zakres_max)

        if zakres_min is not None and zakres_max is not None and zakres_min < zakres_max:
            break
        else:
            print("Błędne dane. Upewnij się, że podałeś poprawne liczby i minimalna wartość jest mniejsza od maksymalnej.")
    
    liczba = random.randint(zakres_min, zakres_max)
    prob = 3  
    
    print("Zgadnij liczbę! Masz 3 próby.")
    
    for i in range(prob):
        zgaduj = input(f"Próba {i + 1}: Podaj liczbę: ")
        zgaduj = sprawdz_liczbe(zgaduj)
        
        if zgaduj is None:
            print("To nie jest liczba. Spróbuj ponownie.")
            continue
        
        if zgaduj < liczba:
            print("Za mało!")
        elif zgaduj > liczba:
            print("Za dużo!")
        else:
            print("Brawo! Zgadłeś liczbę!")
            break
    else:
        print(f"Nie udało się. Wylosowana liczba to {liczba}.")

zgadnij_liczbe()
