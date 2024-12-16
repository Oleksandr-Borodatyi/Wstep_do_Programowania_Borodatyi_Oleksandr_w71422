#Zadanie 4

from datetime import datetime

def dni_od_do(lab_date, kolokwium_date):
    
    dzisiaj = datetime.now() 

    lab_date = datetime.strptime(lab_date, "%d-%m-%Y")
    kolokwium_date = datetime.strptime(kolokwium_date, "%d-%m-%Y")

    dni_od_lab = (dzisiaj - lab_date).days
    dni_do_kolokwium = (kolokwium_date - dzisiaj).days

    lab_date_formatted = lab_date.strftime("%d %B %Y")
    kolokwium_date_formatted = kolokwium_date.strftime("%d %B %Y")

    print(f"Ostatnie laboratoria były: {lab_date_formatted} ({dni_od_lab} dni temu).")
    if dni_do_kolokwium >= 0:
        print(f"Do kolokwium pozostało: {dni_do_kolokwium} dni (data: {kolokwium_date_formatted}).")
    else:
        print(f"Kolokwium już się odbyło ({abs(dni_do_kolokwium)} dni temu, data: {kolokwium_date_formatted}).")

try:
    ostatnie_laby = input("Podaj datę ostatnich laboratoriów (dd-mm-yyyy): ")
    kolokwium = input("Podaj datę kolokwium (dd-mm-yyyy): ")
    dni_od_do(ostatnie_laby, kolokwium)
except ValueError:
    print("Proszę podać poprawne daty w formacie dd-mm-yyyy.")
