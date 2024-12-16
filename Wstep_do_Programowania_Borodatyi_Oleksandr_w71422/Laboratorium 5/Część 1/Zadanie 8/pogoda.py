# pogoda.py

import temperatura  

#A 
celsius_1 = 21
fahrenheit = temperatura.c_to_f(celsius_1)
print(f"{celsius_1} stopni Celsjusza to {fahrenheit} stopni Fahrenheita.")

#B
fahrenheit_2 = 89
celsius = temperatura.f_to_c(fahrenheit_2)
print(f"{fahrenheit_2} stopni Fahrenheita to {celsius} stopni Celsjusza.")

#C
celsius_3 = 35
kelvins = temperatura.c_to_k(celsius_3)
print(f"{celsius_3} stopni Celsjusza to {kelvins} stopni Kelvina.")
