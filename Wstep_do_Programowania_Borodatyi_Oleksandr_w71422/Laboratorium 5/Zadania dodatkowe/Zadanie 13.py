# Zadanie 13

import datetime

def dzien_roku(rok, miesiac, dzien):
    data = datetime.date(rok, miesiac, dzien)
    poczatek_roku = datetime.date(rok, 1, 1)
    return (data - poczatek_roku).days + 1

def numer_tygodnia(rok, miesiac, dzien):
    data = datetime.date(rok, miesiac, dzien)
    return data.isocalendar()[1]

def daty_2_tygodnie(rok, miesiac, dzien):
    data = datetime.date(rok, miesiac, dzien)
    dwa_tygodnie_przed = data - datetime.timedelta(weeks=2)
    dwa_tygodnie_po = data + datetime.timedelta(weeks=2)
    return dwa_tygodnie_przed, dwa_tygodnie_po

def najblizsza_niedziela(rok, miesiac, dzien):
    data = datetime.date(rok, miesiac, dzien)
    dni_do_niedzieli = 6 - data.weekday()  
    return data + datetime.timedelta(days=dni_do_niedzieli)

def czas_unixowy(rok, miesiac, dzien):
    data = datetime.date(rok, miesiac, dzien)
    godzina = datetime.datetime(rok, miesiac, dzien, 0, 0, 0)  
    return godzina.timestamp()

def main():
    rok = int(input("Podaj rok: "))
    miesiac = int(input("Podaj miesiąc: "))
    dzien = int(input("Podaj dzień: "))

    dzien_roku_result = dzien_roku(rok, miesiac, dzien)
    print(f"Dzień roku: {dzien_roku_result}")

    numer_tygodnia_result = numer_tygodnia(rok, miesiac, dzien)
    print(f"Numer tygodnia: {numer_tygodnia_result}")

    dwa_tygodnie_przed, dwa_tygodnie_po = daty_2_tygodnie(rok, miesiac, dzien)
    print(f"Data 2 tygodnie przed: {dwa_tygodnie_przed}")
    print(f"Data 2 tygodnie po: {dwa_tygodnie_po}")

    niedziela = najblizsza_niedziela(rok, miesiac, dzien)
    print(f"Najbliższa niedziela: {niedziela}")

    czas_unix = czas_unixowy(rok, miesiac, dzien)
    print(f"Czas unixowy dla podanej daty: {czas_unix}")

if __name__ == "__main__":
    main()
