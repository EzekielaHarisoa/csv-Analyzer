import csv
from analyserNotes import analyserNotes
from statistique import compterCategories

path = "data/students.csv"

notes = []
villes = []

with open(path, mode="r", encoding="utf-8") as file:
    contenu = csv.DictReader(file)

    for etudiant in contenu:
        notes.append(etudiant.get("note"))
        villes.append(etudiant.get("ville"))    

resultats = analyserNotes(notes)

if resultats is None:
    print("Aucune note valide.")
else:
    print("\n===== ANALYSE DES NOTES =====")

    for nom, valeur in resultats.items():
        print(f"{nom} : {valeur}")


resultats = compterCategories(villes)

for ville, nombre in resultats.items():
    print(f"{ville} : {nombre}")        