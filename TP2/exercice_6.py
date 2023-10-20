L = [1, 4, 0, 2, 1, 4, 2, 100]
print(L)
n = int(input("Donner un nombre: "))

while(L.count(n) != 0):
    L.remove(n)

print(L)