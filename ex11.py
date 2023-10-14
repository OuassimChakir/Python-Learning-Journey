poid = float(input("Donner le poid : "))
taille2 = float(input("Donner taille2 : "))

imc = poid/taille2

imcLists = [
    {"imc": imc > 40, "Interp": "obésité morbide ou massive"},
    {"imc": imc > 35 and imc <= 40 , "Interp": "obésité sévère"},
    {"imc": imc > 30 and imc <= 35, "Interp": "obésité modérée "},
    {"imc": imc > 25 and imc <= 30, "Interp": "Surpoids"},
    {"imc": imc > 18.5 and imc <= 25, "Interp": "corpulence normale"},
    {"imc": imc > 16.5 and imc <= 18.5, "Interp": "Maigreur"},
    {"imc": imc <= 16.5, "Interp": "Famine"},
]

for element in imcLists:
    if(element["imc"]):
        print(element["Interp"])