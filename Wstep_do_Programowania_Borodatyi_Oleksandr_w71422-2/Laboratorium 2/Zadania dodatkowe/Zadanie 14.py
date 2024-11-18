# Zadanie 14

# Program z wykorzystaniem continue:
import math

while True:
    try:
        # Pobranie zmiennej dana od użytkownika
        dana = input("Podaj liczbę (lub wpisz cokolwiek innego, aby zakończyć): ")
        
        # Sprawdzenie, czy dana jest liczbą całkowitą
        dana = int(dana)
        
        if dana >= 0:
            print("To jest liczba dodatnia.")
            print(f"Pierwiastek kwadratowy z {dana} wynosi: {math.sqrt(dana)}")
            continue  # Przejdź do kolejnej iteracji, ponowne wczytanie zmiennej
        else:
            break  # Przerywamy pętlę, gdy liczba jest ujemna
    except ValueError:
        print("Nieprawidłowy format. Program zakończony.")
        break  # Przerywamy pętlę w przypadku błędnego wejścia

print("Dziękujemy za skorzystanie z naszej aplikacji.")


# Program bez wykorzystania continue:
import math

while True:
    try:
        # Pobranie zmiennej dana od użytkownika
        dana = input("Podaj liczbę (lub wpisz cokolwiek innego, aby zakończyć): ")
        
        # Sprawdzenie, czy dana jest liczbą całkowitą
        dana = int(dana)
        
        if dana >= 0:
            print("To jest liczba dodatnia.")
            print(f"Pierwiastek kwadratowy z {dana} wynosi: {math.sqrt(dana)}")
        else:
            print("Dziękujemy za skorzystanie z naszej aplikacji.")
            break  # Przerywamy pętlę, gdy liczba jest ujemna
    except ValueError:
        print("Nieprawidłowy format. Program zakończony.")
        break  # Przerywamy pętlę w przypadku błędnego wejścia
