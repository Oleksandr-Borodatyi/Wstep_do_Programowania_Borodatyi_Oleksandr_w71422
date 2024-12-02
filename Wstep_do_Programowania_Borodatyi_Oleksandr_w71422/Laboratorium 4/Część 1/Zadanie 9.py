# Zadanie 9

n = float(input("Podaj liczbe: "))

def Fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return  Fib(n-1)+Fib(n-2)

print(Fib(n))