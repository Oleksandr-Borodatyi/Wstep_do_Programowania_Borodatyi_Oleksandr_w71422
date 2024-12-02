#Zadanie 8
#Czy pełnoletni?
#>= 18

wiek = int(input("Ilemasz lat?"))

if (wiek > 0) and (wiek <150) :
    if wiek >= 18:
        print("Jesteś pełnoletni")
    else:
        print("Jesteś dzieckiem")
else:
    print("Podane dane są niepoprawne")

#złe odpowiedzi:
#0
#liczby ujemne
#>150
