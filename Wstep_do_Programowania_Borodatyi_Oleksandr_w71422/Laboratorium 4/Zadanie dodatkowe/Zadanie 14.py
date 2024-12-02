#Zadanie 14

def nwd(a, b):
    
    while b != 0:
        a, b = b, a % b  
    return a

print(nwd(int(input("Pierwsza liczba: ")), int(input("Druga liczba: "))))  