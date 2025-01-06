#Zadanie 7

import pandas as pd
import matplotlib.pyplot as plt

# Przykładowe dane sprzedaży
sales_data = {
    'Kategoria': ['Elektronika', 'Odzież', 'Jedzenie', 'Książki', 'Inne'],
    'Sprzedaż': [5000, 3000, 4000, 2000, 1000]
}

# Tworzenie Data Frame
data_df = pd.DataFrame(sales_data)

# Obliczanie procentowego udziału
data_df['Procent'] = (data_df['Sprzedaż'] / data_df['Sprzedaż'].sum()) * 100

# Generowanie wykresu kołowego
plt.figure(figsize=(8, 6))
plt.pie(data_df['Sprzedaż'], labels=data_df['Kategoria'], autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title('Procentowy udział kategorii w całkowitej sprzedaży')
plt.show()
