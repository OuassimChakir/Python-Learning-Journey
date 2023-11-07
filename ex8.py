notes = []
for i in range(0, 4):
    note = float(input(f"Saisir la note {i+1}: "))
    coef = int(input(f"Saisir la coef {i+1}: "))
    notes.insert(i, {"note": note, "coef": coef})

i = 0
totalNotes = totalCoef = 0
for note in notes:
    i += 1
    print(f"Note {i} :",note["note"])
    print("Coefficient :",note['coef'])
    totalNotes += note["note"]*note['coef']
    totalCoef += note["coef"]
moy = totalNotes/totalCoef
if(moy >= 10):
    result = "validé"
elif(moy < 10 and moy >= 7):
    result = "rattrapage"
else:
    result = "non validé"

print("La Moyenne des",i,"Notes est: ",moy,", semestre", result)

#moy >= 10 and "validé" or "non validé"
