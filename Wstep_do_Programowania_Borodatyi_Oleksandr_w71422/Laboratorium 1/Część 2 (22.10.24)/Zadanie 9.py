#Zadanie 9

wiek = int(input("Ile masz lat?"))

if (wiek > 0) and (wiek < 150):
    if ( wiek > 4) and ( wiek < 18):
        print("Bilet kosztuje 10 zł")
    else:
        if (wiek < 4):
            print("Bilet jest zadarmo")
        else:
            czy_student = input("Czy jesteś studentem? (tak/nie):").strip().lower()
            if (czy_student == "tak"):
                print("Bilet kosztuje 15 zł")
            else:
                print("Bilet kosztuje 20 zł")
else:
    print("Podane dane są niepoprawne")