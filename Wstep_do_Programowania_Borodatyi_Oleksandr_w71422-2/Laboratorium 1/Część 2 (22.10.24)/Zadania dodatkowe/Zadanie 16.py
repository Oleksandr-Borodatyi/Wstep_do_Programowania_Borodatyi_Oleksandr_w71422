# Pobranie długości boków trójkąta od użytkownika
a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))
c = float(input("Podaj długość boku c: "))

# Sprawdzenie, czy trójkąt może istnieć
if a + b > c and a + c > b and b + c > a:
    # Obliczenie obwodu trójkąta
    obwod = a + b + c
    print("Obwód trójkąta wynosi:", obwod)
    
    # Obliczenie pola trójkąta (wzór Herona bez zbędnych funkcji)
    s = obwod / 2  # półobwód
    pole = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # pierwiastek za pomocą potęgi 0.5
    print("Pole trójkąta wynosi:", pole)
else:
    print("Podane długości boków nie tworzą trójkąta.")
