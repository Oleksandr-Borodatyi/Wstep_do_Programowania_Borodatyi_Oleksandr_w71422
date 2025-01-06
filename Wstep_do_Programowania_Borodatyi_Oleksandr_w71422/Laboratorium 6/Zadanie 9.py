#Zadanie 9

import pandas as pd
import matplotlib.pyplot as plt

# Dane studentów
students_data = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25]
}

# Tworzenie Data Frame
students_df = pd.DataFrame(students_data)

# Generowanie histogramu
plt.figure(figsize=(8, 6))
plt.hist(students_df['Ocena'], bins=[2, 3, 4, 5, 6], color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Rozkład ocen studentów')
plt.xlabel('Ocena')
plt.ylabel('Liczba studentów')
plt.xticks([2.5, 3.5, 4.5, 5.5], labels=['2-3', '3-4', '4-5', '5-6'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
