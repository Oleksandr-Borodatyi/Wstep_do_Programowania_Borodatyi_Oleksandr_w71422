# Definiowanie nazwy pliku
nazwa_pliku = "przyklad.xlsx"

# Sprawdzenie, czy plik jest arkuszem Excel za pomocą prostszego porównania
# Jeśli ostatnie 4 znaki to ".xls" lub ostatnie 5 znaków to ".xlsx", to plik jest uznawany za arkusz Excel
if nazwa_pliku[-4:] == ".xls" or nazwa_pliku[-5:] == ".xlsx":
    print("Plik jest arkuszem Excel.")
else:
    print("Plik nie jest arkuszem Excel.")

