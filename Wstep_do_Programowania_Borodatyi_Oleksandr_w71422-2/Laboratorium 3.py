"""Laboratorium 3
05.11.24
Część 1
Listy/Zbiory"""
from IPython.extensions.autoreload import append_obj
from mpmath.libmp import round_int

#Zadanie 1
'''list = ["Aleksandr", "Mykyta", "Piotrek", "Vladyslav"]'''


#A
#list=sorted(list)

#B
"""list.append("Serhii")
list.append("Ewa")
ona =list.pop()
print(ona)"""

#C
"""
list.insert(2, "Gosia")

#D
list.reverse()
print(list*2)

print(list)
for imie in list:
    print(imie,end =" ")"""
"""    
# Zadanie 4
lista =[ "adsfk", "ah;fki",";ahf"]
krotka = tuple(lista)
print(krotka)
suma =0
sk = 0
skt = 0
s=int(input('Podaj minimalny rozmiar słowa: '))
slowa = []

for el in krotka:
    #B
    #suma += len(el)
    for z in el:
        if z=="k" : sk+=1       
    #C
        #1
    #if "kt" in el: skt+=1
        #2
   
    if el.find("kt") !=0: skt+=1
    
    #D
    if len(el) >= s:
        slowa.append(el)
        
        
print(f"Liczba znaków w kortce: {suma}")
print(f"w krotce znależono {sk} wystąpień k")
print(f"w krotce znależono {skt} wystąpień kt")
print(f"Słowa  odłudości większej niż {s}, to:", end=" ")
for s in slowa: print(s, end=' ')

import random
n= 3
x=6
lista =[]
slowo=""
długość_słowa = 0

for i in range(n):
    
    lista.append(?)"""

#Zadanie 5
#Lista zakupów
"""suma = 0
zakupy={"chleb": 5.0, "masło": 7.0, "woda": 2.0, "czekolada": 12.0, "czipsy": 12.0}
for el in zakupy:
    suma+= zakupy[el]
    print(f"{el} za {zakupy[el]} zł")
print(f"Za zakupy zapłacimy:{suma}")"""

#Zadanie 7

X={5,6,1,8}
Y={3,5,7,9,1,4,6}

#A
print( 5 in X)

#B
print(X.issubset(Y))

#D
print(X.union(Y))

#E
print(Y.difference(X))

