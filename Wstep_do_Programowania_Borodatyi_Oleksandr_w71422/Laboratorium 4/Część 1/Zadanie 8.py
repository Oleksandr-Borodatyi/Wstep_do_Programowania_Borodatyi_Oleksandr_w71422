# Zadanie 8

def potega(a, n):

    if n == 0:
        return 1 
    elif n > 0:
        return a * potega(a, n - 1)  
    else:
        return 1 / potega(a, -n) 

# Przykłady użycia
print(potega(int(input("Liczba: ")), int(input("Potęga: "))))   