# Pobieranie danych od użytkownika
bok_a= int(input("jaka długość boka a?"))
bok_b= int(input("jaka długość boka b?"))

# Obliczenia
pole_prostokąta=bok_a*bok_b
obwód_prostokąta=2*(bok_a+bok_b)

# Wyświetlanie wyników
print(f"Pole prostokąta: {pole_prostokąta}" )
print(f"Obwód prostokąta: {obwód_prostokąta}")

# Funkcja input() pozwala na pobieranie danych od użytkownika bezpośrednio z klawiatury.
# Użytkownik wprowadza dane po wyświetleniu pytania w konsoli.
# Wynik tej funkcji jest zawsze typu string, więc konieczna jest konwersja do odpowiedniego typu liczbowego (np. int lub float)