#Zadanie 1
list = ["Aleksandr", "Mykyta", "Piotrek", "Vladyslav"]

#A
list=sorted(list)

#B
list.append("Serhii")
list.append("Ewa")
ona =list.pop()
print(ona)

#C

list.insert(2, "Gosia")

#D
list.reverse()
print(list*2)

print(list)
for imie in list:
    print(imie,end =" ")