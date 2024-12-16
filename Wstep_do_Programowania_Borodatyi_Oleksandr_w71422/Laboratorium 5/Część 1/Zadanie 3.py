# Zadanie 3

import time

def sekundnik(czas):
    
    while czas > 0:  
        print(f"Pozostało: {czas} sekund")  
        time.sleep(1)  
        czas -= 1  
    print("Czas upłynął!") 

try:
    czas = int(input("Podaj czas odliczania w sekundach: "))  
    if czas > 0: 
        sekundnik(czas)  
    else:
        print("Czas musi być liczbą dodatnią!")  
except ValueError:
    print("Proszę podać poprawną liczbę całkowitą!")  
