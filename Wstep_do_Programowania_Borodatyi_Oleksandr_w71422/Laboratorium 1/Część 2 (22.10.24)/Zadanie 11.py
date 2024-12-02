# Zadanie 11

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 - 4*a*c
if (delta < 0):
    print("Rozwiązanie jest niemożliwe")
else:
    if ( delta == 0):
        print (f"Pierwiastek = {-b/(2*a)}")
    else:
        print(f"Pierwiastek 1: {(-b-delta*0.5)/(2*a)}")
        print(f"Pierwiastek 2: {(-b + delta * 0.5) / (2 * a)}")