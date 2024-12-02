# Zadanie 12

def okresl_plec(imie):
    
    imiona_kobiece = ["Anna", "Kasia", "Maria", "Joanna", "Agnieszka"]
    
    imiona_meskie = ["Piotr", "Jan", "Krzysztof", "Marek", "Tomasz"]

    if imie in imiona_kobiece:
        return "kobieta"
    elif imie in imiona_meskie:
        return "mężczyzna"
    else:
        return "nieznana płeć"

imiona = ["Anna", "Piotr", "Joanna", "Tomasz", "Ewa"]

slownik_imion = {imie: okresl_plec(imie) for imie in imiona}

print(slownik_imion)
