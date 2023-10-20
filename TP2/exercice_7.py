L = [1, 4, 6, 2, 1, 4, 2, 10]
print(L)

for element in L:
    while(L.count(element) != 1):
        L.remove(element)
L.sort()

print(L)