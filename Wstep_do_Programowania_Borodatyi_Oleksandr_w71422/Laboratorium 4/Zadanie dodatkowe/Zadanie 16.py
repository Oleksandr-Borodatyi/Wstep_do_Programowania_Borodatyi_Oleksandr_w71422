# Zadanie 16

def sa_anagramami(slowo1, slowo2):
    """
    Funkcja sprawdza, czy dwa słowa są anagramami.
    Anagramy to słowa zawierające te same litery w innej kolejności.
    """
    slowo1 = slowo1.replace(" ", "").lower()
    slowo2 = slowo2.replace(" ", "").lower()

    return sorted(slowo1) == sorted(slowo2)

print(sa_anagramami(input("Pierwsze słowo: "), input("Drugie słowo: "))) 