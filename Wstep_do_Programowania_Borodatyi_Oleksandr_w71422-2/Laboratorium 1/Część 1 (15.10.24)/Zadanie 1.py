# Wyniki i analiza typów operacji
print(type(1 + 2))       # int - dodawanie dwóch liczb całkowitych zwraca typ int
print(type(1 + 4.5))     # float - dodawanie liczby całkowitej i zmiennoprzecinkowej zwraca typ float
print(type(3 / 2))       # float - dzielenie zawsze zwraca wynik float
print(type(4 / 2))       # float - nawet gdy dzielenie jest bez reszty, wynik to float
print(type(3 // 2))      # int - dzielenie całkowitoliczbowe zwraca typ int
print(type(-3 // 2))     # int - wynik dzielenia całkowitoliczbowego z liczbą ujemną jest zaokrąglany w dół i zwraca int
print(type(11 % 2))      # int - operator % zwraca resztę z dzielenia, która jest typu int
print(type(2 ** 10))     # int - potęgowanie liczb całkowitych zwraca int
print(type(8 ** (1/3)))  # float - potęgowanie do ułamkowego wykładnika zwraca float

#   Operatory:
# + — dodawanie liczb.
# / — dzielenie, wynik zawsze float.
# // — dzielenie całkowitoliczbowe, ignoruje resztę, zwraca int.
# % — reszta z dzielenia (modulo).
# ** — potęgowanie, zwraca float, jeśli wykładnik jest ułamkowy.
