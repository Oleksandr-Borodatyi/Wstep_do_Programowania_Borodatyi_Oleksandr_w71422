# Zadanie 1
#  
#A

import random

def szczesliwy_numerek(liczba_osob):
    
    return random.randint(1, liczba_osob)

liczba_osob = int(input("Podaj liczbę osób w grupie: "))
numer = szczesliwy_numerek(liczba_osob)
print(f"Szczęśliwy numerek dla grupy to: {numer}")


#B

def szczesliwy_rocznik(roczniki):
    
    return random.choice(roczniki)

roczniki = list(map(int, input("Podaj roczniki urodzenia w grupie, oddzielone przecinkami: ").split(",")))
wylosowany_rocznik = szczesliwy_rocznik(roczniki)
print(f"Szczęśliwy rocznik to: {wylosowany_rocznik}")


#C 

def losowanie_totolotka():
    
    liczby = list(range(1, 50))  
    wylosowane = random.sample(liczby, 6) 
    return wylosowane

wynik = losowanie_totolotka()
print(f"Wylosowane liczby w totolotku to: {wynik}")
