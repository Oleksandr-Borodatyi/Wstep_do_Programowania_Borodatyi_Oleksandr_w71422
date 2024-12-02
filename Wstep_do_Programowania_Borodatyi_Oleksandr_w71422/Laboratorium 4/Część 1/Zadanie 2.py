# Zadanie 2

import math

def Pole_trapezu(a, b, h):
    if a <= 0 or b <= 0 or h <= 0:
        print(f"Blęne dane!")
    else:
        print(f"Pole trapezu: {((a+b/2)*h)}")

Pole_trapezu(int(input("Wprowadż dane o a: ")),
             int(input("Wprowadż dane o b: ")),
             int(input("wprowadż dane o h: ")))