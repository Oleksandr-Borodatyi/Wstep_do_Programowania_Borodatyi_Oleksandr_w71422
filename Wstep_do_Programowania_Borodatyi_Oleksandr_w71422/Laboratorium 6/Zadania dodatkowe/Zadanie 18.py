# Zadanie 18

import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych z pliku Excel do ramki danych Pandas
# Plik "sales_data.xlsx" powinien znajdować się w tym samym katalogu co skrypt
data = pd.read_excel("sales_data.xlsx")

# Wyświetlenie podstawowych informacji o danych
print("Podstawowe informacje o danych:")
print(data.info())
print("\nPodgląd danych:")
print(data.head())

# Analiza podstawowych statystyk dotyczących danych
print("\nPodstawowe statystyki dla danych liczbowych:")
print(data.describe())

# Obliczenie sumy sprzedaży i średniej ceny produktów
total_sales = data["Sales"].sum()
average_price = data["Price"].mean()
print(f"\nSuma sprzedaży: {total_sales}")
print(f"Średnia cena produktu: {average_price}")

# Grupowanie danych według kategorii produktów
category_sales = data.groupby("Category")["Quantity"].sum()

# Tworzenie wykresu słupkowego dla ilości sprzedanych produktów w kategoriach
category_sales.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Ilość sprzedanych produktów w poszczególnych kategoriach")
plt.xlabel("Kategoria")
plt.ylabel("Ilość sprzedanych produktów")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Tworzenie wykresu punktowego dla zależności między ceną a ilością sprzedaży
plt.scatter(data["Price"], data["Quantity"], color="red", alpha=0.7)
plt.title("Zależność między ceną a ilością sprzedanych produktów")
plt.xlabel("Cena")
plt.ylabel("Ilość sprzedanych produktów")
plt.grid(True)
plt.tight_layout()
plt.show()

# Wnioski:
print("\nWnioski:")
print("- Najbardziej zyskowne kategorie produktów można zidentyfikować na podstawie sumy ilości sprzedanych produktów w każdej kategorii (wykres słupkowy).")
print("- Wykres punktowy pokazuje, czy istnieje zależność między ceną a ilością sprzedaży. Jeśli punkty są skoncentrowane w określonych obszarach, może to wskazywać na korelacje.")
print("- Na podstawie analizy danych warto przeprowadzić dodatkowe badania, np. analizę rentowności poszczególnych kategorii.")
