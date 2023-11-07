a = int(input("Donner a: "))
b = int(input("Donner b: "))

if((a < 0 and b < 0) or (a > 0 and b > 0)):
    print(f"le produit de {a} et {b} est positif")
elif((a<0 and b>0) or (a>0 and b<0)):
    print(f"le produit de {a} et {b} est negatif")
else:
    print(f"le produit de {a} et {b} est null")