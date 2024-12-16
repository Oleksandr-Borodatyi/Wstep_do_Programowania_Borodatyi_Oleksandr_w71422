# Zadanie 2

import math
import cmath  # do obliczeń zespolonych

#A √81
wynik_a = math.sqrt(81)
print(f"a) √81 = {wynik_a}")

#B 810
wynik_b = 810
print(f"b) 810 = {wynik_b}")

#C √2 + √3 + √6
wynik_c = math.sqrt(2) + math.sqrt(3) + math.sqrt(6)
print(f"c) √2 + √3 + √6 = {wynik_c:.3f}")

#D √−5
wynik_d = cmath.sqrt(-5)  # używamy cmath, bo √-5 wymaga liczb zespolonych
print(f"d) √−5 = {wynik_d}")

#E 3√125
wynik_e = 3 * math.sqrt(125)
print(f"e) 3√125 = {wynik_e}")
