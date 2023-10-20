L = [1, 4, 6, 2, 1, 4, 2, 10]
print(L)

n = int(input("Donner un nombre: "))
nbOcc = L.count(n)
print("Le nombre d'occurences dans la liste est:",nbOcc)
if nbOcc != 0:
    print("La position de chaque occurence respectivement: ")
    for index, value in enumerate(L):
        if value == n :
            print(index, end=", ")