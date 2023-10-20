x = int(input("Saisir un nombre: "))
while(x > 9 or x < 1):
    x = int(input("Saisir un nombre: "))
sum = (x) + (x*11) + (x*111) + (x*1111)
print((x),"+",(x*11),"+",(x*111),"+",(x*1111),"=",sum)