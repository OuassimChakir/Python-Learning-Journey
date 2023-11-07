grades = [
    {"grade" : 'A', "tarif" : 200, "prime" : 1000, "nbHeurs" : 20},
    {"grade": 'B', "tarif": 150, "prime": 800, "nbHeurs": 20},
    {"grade": 'C', "tarif": 120, "prime": 500, "nbHeurs": 15},
    {"grade": 'D', "tarif": 100, "prime": 350, "nbHeurs": 15},
    {"grade": 'E', "tarif": 80, "prime": 100, "nbHeurs": 10}
]

grade = input("Saisir votre Grade => ")
nbHeurs = int(input("Saisir le nombre d'heurs => "))
salaire = 0
for element in grades:
    if(element["grade"] == grade):
        salaire = (element["tarif"]*nbHeurs) + (element["prime"]*(nbHeurs/element["nbHeurs"]))

print(salaire)