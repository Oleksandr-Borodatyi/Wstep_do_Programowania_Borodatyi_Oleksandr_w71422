# Zadanie 17

import requests
import pandas as pd
import matplotlib.pyplot as plt

# Twój klucz API (wstaw tutaj swój klucz)
api_key = 'twoj_klucz_api'

# Funkcja do pobrania danych pogodowych z OpenWeatherMap
def get_weather_data(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

# Pobieranie danych dla kilku miast
cities = ['Warsaw', 'Krakow', 'Gdansk', 'Wroclaw', 'Poznan']
weather_data = []

for city in cities:
    data = get_weather_data(city, api_key)
    weather_data.append({
        'city': city,
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'wind_speed': data['wind']['speed'],
        'weather': data['weather'][0]['description'],
        'timestamp': pd.to_datetime(data['dt'], unit='s')  # Przekształcamy czas w sekundach na datę
    })

# Wczytanie danych do Pandas DataFrame
df = pd.DataFrame(weather_data)

# a) Wyświetlenie podstawowych informacji o danych
print("Podstawowe informacje o danych:")
print(df.info())

# b) Statystyki opisowe
print("\nStatystyki opisowe:")
print(df.describe())

# c) Sprawdzanie brakujących danych
print("\nBrakujące dane:")
print(df.isnull().sum())

# d) Obliczenie średnich temperatur dla różnych miast
print("\nŚrednia temperatura dla różnych miast:")
mean_temperatures = df.groupby('city')['temperature'].mean()
print(mean_temperatures)

# e) Wizualizacja danych

# f) Wykres liniowy zmiany temperatury w czasie
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['temperature'], marker='o', color='b')
plt.title('Zmiana temperatury w czasie')
plt.xlabel('Czas')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.show()

# g) Wykres punktowy temperatury w różnych lokalizacjach
plt.figure(figsize=(8, 6))
plt.scatter(df['city'], df['temperature'], color='r')
plt.title('Temperatura w różnych lokalizacjach')
plt.xlabel('Miasto')
plt.ylabel('Temperatura (°C)')
plt.show()

# h) Dodanie tytułów, etykiet osi i legendy
# (To jest już zawarte w kodzie wykresów powyżej)

# i) Wnioski
print(''' Wnioski należy przygotować na podstawie wyników analizy danych i wykresów:

 - Można zidentyfikować, czy istnieją trendy w zmianie temperatury w czasie.
 
 - Można sprawdzić, czy są różnice między temperaturą w różnych lokalizacjach. ''')

