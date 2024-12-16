# Zadanie 12

import math

def pole_trojkata(a, b, kat):
    if a <= 0 or b <= 0:
        return "Boki trójkąta muszą być dodatnie."
    
    if kat <= 0 or kat >= 90:
        return "Kąt musi być ostrym kątem (mniejszym niż 90 stopni)."
    
    kat_radiany = math.radians(kat) 
    pole = 0.5 * a * b * math.sin(kat_radiany) 
    return pole

a = float(input("Podaj długość pierwszego boku trójkąta: "))
b = float(input("Podaj długość drugiego boku trójkąta: "))
kat = float(input("Podaj kąt między bokami w stopniach: "))

pole = pole_trojkata(a, b, kat)
print(f"Pole trójkąta wynosi: {pole}")
