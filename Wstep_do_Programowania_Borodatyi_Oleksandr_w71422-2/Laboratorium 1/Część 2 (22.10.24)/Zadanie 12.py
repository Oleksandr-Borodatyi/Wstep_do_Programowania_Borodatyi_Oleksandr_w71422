#Zadanie 12

x = int(input("Argument dla funkcji: "))
typ_funkcji = input("Typ funkcji(a,b lub c): ")

if typ_funkcji == "a":
    if (x < 0) :
       print(f"= {-3*x}")
    if (x == 0) :
       print(f"= {x}")
    if (x > 0) :
       print(f"= {2*x}")

if typ_funkcji == "b":
    if (x < 1) :
       print(f"= {x}")
    if (x >= 1) :
       print(f"= {x**2}")

if typ_funkcji == "c":
    if (x < 2) :
       print(f"= {x-4}")
    if (x == 2) :
       print(f"= {8}")
    if (x > 2) :
       print(f"= {2+x}")