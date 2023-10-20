choice = 0
while (choice != 1) and (choice != 2):
    choice = int(input("1. euro en mad\n2. mad en euro\nSelect: "))

nb = 1
if choice == 1:
    while nb >= 0 :
        nb = float(input("Entrer la valeur en Euro: "))
        if nb < 0: break
        print(nb,"€ = ",(nb*10.86),"mad")
elif choice == 2:
    while nb >= 0 :
        nb = float(input("Entrer la valeur en DH: "))
        if nb < 0: break
        print(nb,"DH = ",(nb*0.092),"€")