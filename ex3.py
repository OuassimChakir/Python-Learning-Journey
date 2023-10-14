distance = float(input("Saisir la distance (km) : "))
temps = int(input("Saisir le temps en minute : "))
if(temps == 0):
    temps = 1
distance *= 1000
temps *= 60
print("La vitesse : ",distance/temps," m/s")