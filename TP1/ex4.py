second = int(input("Saisir le nombre des secondes : "))
totalSecond = second
heurs = int(second/3600)
second -= heurs*3600
minutes = int(second/60)
second -= minutes*60

print(totalSecond,"Secondes =",heurs,"H",minutes,"MIN",second,"sec")
