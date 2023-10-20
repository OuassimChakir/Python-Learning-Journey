L = [1, -30, 0, -2, 500, 4, 2, 100]
L.sort()
print(L)
n = int(input("Donner un nombre: "))
i = 0
for element in L:
    if(n < element):
        break
    else:
        i = i + 1
L.insert(i, n)
print(L)