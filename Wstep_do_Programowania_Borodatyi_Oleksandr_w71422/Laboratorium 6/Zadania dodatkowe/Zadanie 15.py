# Zadanie 15

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Tworzenie danych studentów
data = {
    "Nr_albumu": [1, 2, 3, 4, 5],
    "Imię": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "Nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "Ocena_1_termin": [4.5, 3.0, 5.0, 4.0, 2.5],
    "Ocena_2_termin": [4.0, 3.5, 4.5, 3.5, 3.0]
}

df = pd.DataFrame(data)

# Obliczanie ostatecznych ocen jako średnia z obu terminów
df["Ocena_ostateczna"] = df[["Ocena_1_termin", "Ocena_2_termin"]].mean(axis=1)

# Tworzenie wykresów
plt.figure(figsize=(10, 6))

# Wykres dla 1. terminu
plt.plot(df["Nr_albumu"], df["Ocena_1_termin"], label="1. Termin", color="blue", linestyle="--", marker="o")

# Wykres dla 2. terminu
plt.plot(df["Nr_albumu"], df["Ocena_2_termin"], label="2. Termin", color="green", linestyle="-.", marker="s")

# Wykres dla ocen ostatecznych
plt.plot(df["Nr_albumu"], df["Ocena_ostateczna"], label="Ocena Ostateczna", color="red", linestyle="-", marker="d")

# Dodanie opisu osi i tytułu
plt.xlabel("Nr Albumu")
plt.ylabel("Ocena")
plt.title("Porównanie ocen studentów z różnych terminów")

# Dostosowanie legendy
plt.legend(title="Legenda", loc="upper left")

# Wyświetlenie siatki
plt.grid(True, linestyle="--", alpha=0.7)

# Wyświetlenie wykresu
plt.show()
