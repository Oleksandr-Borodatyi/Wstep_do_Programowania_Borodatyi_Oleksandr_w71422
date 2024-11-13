# a. int(3.0)
print(int(3.0))  # Wynik: 3
# Konwersja liczby zmiennoprzecinkowej (float) do liczby całkowitej (int). Część dziesiętna jest ignorowana.

# b. float(3)
print(float(3))  # Wynik: 3.0
# Konwersja liczby całkowitej (int) na liczbę zmiennoprzecinkową (float).

# c. float("3")
print(float("3"))  # Wynik: 3.0
# Konwersja ciągu tekstowego ("3") na liczbę zmiennoprzecinkową (float). Tekst musi być liczbą.

# d. str(12.4)
print(str(12.4))  # Wynik: '12.4'
# Konwersja liczby zmiennoprzecinkowej (float) na ciąg znaków (str).

# e. bool(0)
print(bool(0))  # Wynik: False
# Konwersja liczby 0 na wartość logiczną (bool). Wartość 0 jest interpretowana jako False.

#   Wyjaśnienie:
# int(): Konwertuje wartość do liczby całkowitej, usuwając część dziesiętną.
# float(): Konwertuje wartość na liczbę zmiennoprzecinkową.
# str(): Konwertuje wartość na ciąg znaków (tekst).
# bool(): Konwertuje wartość na typ logiczny. W Pythonie 0 jest interpretowane jako False, a wszystkie inne liczby jako True.