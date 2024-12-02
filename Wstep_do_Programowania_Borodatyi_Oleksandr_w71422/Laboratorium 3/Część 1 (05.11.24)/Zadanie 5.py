#Zadanie 5
#Lista zakupów

suma = 0
zakupy={"chleb": 5.0, "masło": 7.0, "woda": 2.0, "czekolada": 12.0, "czipsy": 12.0}

for el in zakupy:

    suma+= zakupy[el]
    print(f"{el} za {zakupy[el]} zł")
    
print(f"Za zakupy zapłacimy:{suma}")