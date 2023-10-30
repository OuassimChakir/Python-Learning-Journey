import random

x = random.randint(1,100)
n = i = 0

while(n != x and i < 7):
    i = i + 1
    n = int(input("Donner un nombre (1 à 100): "))
    if n < 1 or n > 100:
        print("Oups, vous avez saisi un nombre en dehors de l'intervalle")
    elif n > x:
        print("Oups, entrez un nombre plus petit")
    elif n < x:
        print("Oups, entrer un nombre plus grand")
    else:
        print("Bravo",n,"est le nombre que j'ai choisit")
        print("Vous l'avez deviné",i,"essais")
        break

if i == 7 :
    print("J'ai gagné, je suis le meilleur, Le nombre que j'ai deviné est",x)
    print("Au revoir!")