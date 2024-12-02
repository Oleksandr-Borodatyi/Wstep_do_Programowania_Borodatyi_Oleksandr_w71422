# Zadanie 1

import math

def Pole_Kola(r):
    if  r <= 0:
        print("Koło o takim o takim promieniu nie istnieje")
    else:
        print(f"Koło o takim promieniu ma takie pole:{math.pi*r**2}")

Pole_Kola(int(input("Wprowadż dane o promieniu r: ")))