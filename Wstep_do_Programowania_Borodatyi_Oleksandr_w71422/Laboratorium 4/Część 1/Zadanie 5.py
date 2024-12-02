# Zadanie 5

lista_liczb = []
def obliczenia(lista_liczb):
    liczba_srednia = 0
    for elements in lista_liczb:
        liczba_srednia += elements
    print(liczba_srednia/len(lista_liczb))
def wprowadzanie_danych():
    while True:
        x = input("Wprowadż dane, jeżeli chcesz skonczyć napisz stop: ")
        if  x != "stop":
            lista_liczb.append(int(x))
        else:
            obliczenia(lista_liczb)
            break

wprowadzanie_danych()