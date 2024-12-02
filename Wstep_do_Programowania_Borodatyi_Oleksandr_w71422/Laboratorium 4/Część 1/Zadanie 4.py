#Zadanie 4

def oblicz_bmi(waga, wzrost):
   
    if wzrost <= 0 or waga <= 0:
        return "Waga i wzrost muszą być większe od zera."

    # Obliczenie BMI
    bmi = waga / (wzrost ** 2)

    # Określenie zakresu BMI
    if bmi < 18.5:
        zakres = "niedowaga"
    elif 18.5 <= bmi < 25:
        zakres = "waga prawidłowa"
    elif 25 <= bmi < 30:
        zakres = "nadwaga"
    else:
        zakres = "otyłość"

    # Zwracanie wyniku
    return f"Twoje BMI wynosi {bmi:.2f}. Jesteś w zakresie: {zakres}."

waga = int(input("Wprowadz wage w kg: "))
wzrost = int(input("Wprowadz wzrost w metrach: "))
print(oblicz_bmi(waga, wzrost))
