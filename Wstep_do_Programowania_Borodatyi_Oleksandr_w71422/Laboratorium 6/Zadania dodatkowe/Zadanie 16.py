# Zadanie 16

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie zbioru danych (Automobile Data Set z UCI)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
columns = [
    "symboling", "normalized_losses", "make", "fuel_type", "aspiration", "num_doors",
    "body_style", "drive_wheels", "engine_location", "wheel_base", "length", "width",
    "height", "curb_weight", "engine_type", "num_cylinders", "engine_size", "fuel_system",
    "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm", "city_mpg",
    "highway_mpg", "price"
]
df = pd.read_csv(url, names=columns, na_values="?")

# a) Informacje o danych
print(df.info())  # Wyświetlenie informacji o zbiorze danych
print(df.describe())  # Wyświetlenie statystyk opisowych

# b) Średnia cena samochodów w zależności od marki
avg_price_by_make = df.groupby("make")["price"].mean().sort_values()  # Grupowanie po marce i obliczanie średniej ceny
plt.figure(figsize=(12, 6))
avg_price_by_make.plot(kind="bar", color="skyblue")  # Wykres słupkowy
plt.title("Średnia cena samochodów w zależności od marki")
plt.xlabel("Marka")
plt.ylabel("Średnia cena")
plt.xticks(rotation=45)
plt.show()

# c) Zależność mocy silnika od zużycia paliwa
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="horsepower", y="city_mpg", hue="body_style", palette="viridis")  # Wykres punktowy
plt.title("Zależność mocy silnika od zużycia paliwa")
plt.xlabel("Moc silnika (horsepower)")
plt.ylabel("Zużycie paliwa (mpg w mieście)")
plt.legend(title="Typ nadwozia")  # Legenda
plt.show()

# d) Zidentyfikuj 5 najczęściej występujących krajów pochodzenia samochodów
# Stworzenie mapy dla powiązania marek z krajami
brand_to_country = {
    'audi': 'Germany', 'bmw': 'Germany', 'chevrolet': 'USA', 'chrysler': 'USA',
    'dodge': 'USA', 'honda': 'Japan', 'mazda': 'Japan', 'mercedes': 'Germany',
    'mitsubishi': 'Japan', 'nissan': 'Japan', 'peugeot': 'France', 'plymouth': 'USA',
    'porsche': 'Germany', 'renault': 'France', 'saab': 'Sweden', 'subaru': 'Japan',
    'toyota': 'Japan', 'volkswagen': 'Germany', 'volvo': 'Sweden'
}

# Dodanie nowej kolumny, która wskazuje kraj pochodzenia
df['country'] = df['make'].str.lower().map(brand_to_country)

# Znalezienie 5 najczęściej występujących krajów i przedstawienie ich rozkładu na wykresie kołowym
top_countries = df['country'].value_counts().head(5)
plt.figure(figsize=(8, 8))
top_countries.plot(kind="pie", autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))  # Wykres kołowy
plt.title("Rozkład najczęstszych krajów pochodzenia samochodów")
plt.ylabel("")  # Usunięcie etykiety z osi Y
plt.show()

# e) Grupowanie danych według kategorii nadwozia
grouped_body = df.groupby("body_style")[["price", "horsepower", "city_mpg"]].mean()  # Grupowanie po typie nadwozia
print(grouped_body)  # Wyświetlenie średnich dla każdej kategorii nadwozia

# f) Dodatkowe analizy
# Wykres: Masa pojazdu w zależności od długości
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="length", y="curb_weight", hue="fuel_type", palette="coolwarm")  # Wykres punktowy
plt.title("Masa pojazdu w zależności od długości")
plt.xlabel("Długość pojazdu")
plt.ylabel("Masa pojazdu")
plt.legend(title="Rodzaj paliwa")  # Legenda dla rodzaju paliwa
plt.show()

# g) Wnioski
print("Wnioski:")
print("- Marka samochodu ma znaczący wpływ na średnią cenę.")
print("- Zależność między mocą silnika a zużyciem paliwa różni się w zależności od kategorii nadwozia.")
print("- Dane pokazują, że popularne marki dominują na rynku, co widać w rozkładzie marek.")
print("- Istnieją widoczne trendy w masie pojazdu w zależności od długości oraz rodzaju paliwa.")

