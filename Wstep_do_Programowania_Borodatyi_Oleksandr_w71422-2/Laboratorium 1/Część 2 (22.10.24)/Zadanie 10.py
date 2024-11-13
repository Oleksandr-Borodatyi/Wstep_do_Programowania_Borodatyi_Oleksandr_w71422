# Zadanie 10

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print( x, y, z)