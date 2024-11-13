# Pobranie znaku od użytkownika
znak = input("Wprowadź jedną literę: ")

# Sprawdzenie, czy użytkownik podał tylko jeden znak i czy jest to litera
if len(znak) == 1 and znak.isalpha():
    # Sprawdzenie, czy litera jest duża
    if 'A' <= znak <= 'Z':  # duża litera
        # Zamiana na małą literę za pomocą kodów ASCII
        zamieniony_znak = chr(ord(znak) + 32)
        print("Zamieniono na małą literę:", zamieniony_znak)
    elif 'a' <= znak <= 'z':  # mała litera
        # Zamiana na dużą literę za pomocą kodów ASCII
        zamieniony_znak = chr(ord(znak) - 32)
        print("Zamieniono na dużą literę:", zamieniony_znak)
else:
    print("Proszę wprowadzić tylko jedną literę.")
