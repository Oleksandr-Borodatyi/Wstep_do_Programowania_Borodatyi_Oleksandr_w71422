# Zadanie 15

def jest_palindromem(slowo):
    
    slowo = slowo.replace(" ", "").lower()
    return slowo == slowo[::-1] 

print(jest_palindromem(input("Wpisz słowo: ")))  
