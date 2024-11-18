# Zadanie 9

# Rozmiar pola gry
width = 6
height = 5

# Pozycje przeciwników i monet
przeciwnicy = [(0, 1), (2, 3), (2, 4), (3, 4)]
monety = [(1, 1), (2, 0), (3, 3), (5, 3)]

# Rysowanie pola gry
for y in range(height):
    for x in range(width):
        # Sprawdzenie czy jest rzeka
        if y == 2:
            print("=", end="")
        # Sprawdzenie czy jest przeciwnik
        elif (x, y) in przeciwnicy:
            print("x", end="")
        # Sprawdzenie czy jest moneta
        elif (x, y) in monety:
            print("*", end="")
        else:
            print(".", end="")
    print()  # Przejście do nowej linii po każdym wierszu
