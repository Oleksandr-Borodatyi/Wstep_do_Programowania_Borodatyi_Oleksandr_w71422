# Pobranie znaku od użytkownika
znak = input("Wprowadź jedną literę: ")

# Sprawdzenie, czy użytkownik podał tylko jeden znak
if len(znak) == 1 and znak.isalpha():
    # Sprawdzenie, czy litera jest duża czy mała
    if 'A' <= znak <= 'Z':  # lub znak.isupper()
        print("Litera jest duża.")
    elif 'a' <= znak <= 'z':  # lub znak.islower()
        print("Litera jest mała.")
else:
    print("Proszę wprowadzić tylko jedną literę.")
