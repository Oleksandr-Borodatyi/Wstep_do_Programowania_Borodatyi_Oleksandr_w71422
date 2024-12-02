# Pobranie liczb od użytkownika
num1 = float(input("Wprowadź pierwszą liczbę: "))
num2 = float(input("Wprowadź drugą liczbę: "))
    
    # Pobranie działania od użytkownika
operation = input("Wprowadź operację (+, -, *, /): ")
    
    # Wykonanie wybranej operacji
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
        # Dodanie sprawdzenia dzielenia przez zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Błąd: dzielenie przez zero!"
else:
    result = "Nieznana operacja"
    
print("Wynik:", result)