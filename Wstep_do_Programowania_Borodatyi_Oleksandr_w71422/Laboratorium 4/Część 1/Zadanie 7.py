#Zadanie 7 

import math

def pole_trojkata(a, b, c):
    """
    Funkcja oblicza pole trójkąta na podstawie długości boków a, b, c
    za pomocą wzoru Herona. Sprawdza, czy podane dane są prawidłowe.
    
    Zwraca pole trójkąta lub komunikat o błędzie, jeśli dane są nieprawidłowe.
    """
    try:
        # Sprawdzenie, czy dane wejściowe są dodatnie
        if a <= 0 or b <= 0 or c <= 0:
            return "Długości boków muszą być większe od zera."

        # Sprawdzenie nierówności trójkąta
        if not (a + b > c and a + c > b and b + c > a):
            return "Podane boki nie spełniają nierówności trójkąta."

        # Obliczenie pola za pomocą wzoru Herona
        s = (a + b + c) / 2  # Połowa obwodu
        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return f"Pole trójkąta wynosi: {pole:.2f}"

    except Exception as e:
        return f"Wystąpił błąd: {str(e)}"

# Przykłady użycia funkcji
print(pole_trojkata(int(input("a: ")),int(input("b: ")),int(input("c: "))))  