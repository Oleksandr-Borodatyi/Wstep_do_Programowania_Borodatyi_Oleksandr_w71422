# Zadanie 5 

import keyword

def sprawdz_slowa(lista_slow):
    
    for slowo in lista_slow:
        if keyword.iskeyword(slowo):
            print(f"'{slowo}' - to jest keyword.")
        else:
            print(f"'{slowo}' - to nie jest keyword.")


slowa = ["for", "print", "break", "done", "bad"]

sprawdz_slowa(slowa)
