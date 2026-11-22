
import csv
from netoyage import analyserNotes
from rapport import exporterRapport
from statistique import compterCategories, detecterDoublons, filtrerEtudiant
from affichage import afficherMenu

path = "data/students.csv"

notes = []
villes = []
colonnesVides = {}
etudiants = []

with open(path, mode="r", encoding="utf-8") as file:
    contenu = csv.DictReader(file)

    for colonne in contenu.fieldnames:
        colonnesVides[colonne] = 0

    for etudiant in contenu:
        notes.append(etudiant.get("note"))
        villes.append(etudiant.get("ville"))
        etudiants.append(etudiant)

        for colonne, valeur in etudiant.items():
            if valeur is None or valeur.strip() == "":
                colonnesVides[colonne] += 1


resultatsNote = analyserNotes(notes)
doublons = detecterDoublons(etudiants)

while True:
    afficherMenu()

    choix = input("\n Votre choix : ").strip()

    if choix == "1":
        print("\n===== ANALYSE DES NOTES =====")

        if resultatsNote is None:
            print("Aucune note valide.")
        else:
            for nom, valeur in resultatsNote.items():
                print(f"{nom} : {valeur}")

    elif choix == "2":
        print("\n===== ANALYSE DES VILLES =====")

        resultatsVille = compterCategories(villes)
        total = sum(resultatsVille.values())

        if total == 0:
            print("Aucune ville valide.")
        else:
            print("\n1 - Effectifs")

            for ville, nombre in resultatsVille.items():
                print(f"{ville} : {nombre}")

            print("\n2 - Pourcentages")

            for ville, nombre in resultatsVille.items():
                pourcentage = nombre / total * 100
                print(f"{ville} : {pourcentage:.2f} %")

    elif choix == "3":
        print("\n===== VALEURS MANQUANTES =====")

        for colonne, nombre in colonnesVides.items():
            print(f"{colonne} : {nombre}")

    elif choix == "4":
        print("\n===== DÉTECTION DES DOUBLONS =====")

        print(f"Nombre de doublons : {len(doublons)}")

        for doublon in doublons:
            print(doublon)

    elif choix == "5":
        print("\n===== FILTRAGE DES ÉTUDIANTS =====")

        villeRecherche = input("Ville recherchée : ")

        etudiantFiltrer = filtrerEtudiant( etudiants, "ville", villeRecherche  )

        print(f"Nombre d'étudiants trouvés : {len(etudiantFiltrer)}")

        for etudiant in etudiantFiltrer:
            print(etudiant)
    
    elif choix == "7":
        texte = "===== RAPPORT CSV ANALYZER =====\n\n"

        texte += "===== ANALYSE DES NOTES =====\n"

        if resultatsNote is None:
            texte += "Aucune note valide.\n"
        else:
            for nom, valeur in resultatsNote.items():
                texte += f"{nom} : {valeur}\n"

        texte += "\n===== ANALYSE DES VILLES =====\n"

        resultatsVille = compterCategories(villes)

        for ville, nombre in resultatsVille.items():
            texte += f"{ville} : {nombre}\n"

        texte += "\n===== VALEURS MANQUANTES =====\n"

        for colonne, nombre in colonnesVides.items():
            texte += f"{colonne} : {nombre}\n"

        texte += "\n===== DOUBLONS =====\n"
        texte += f"Nombre de doublons : {len(doublons)}\n"

        exporterRapport(texte)

    elif choix == "6":
         print("Merci d'avoir utilisé CSV Analyzer !")
         break
    else:
        print("Choix invalide. Réessayez.")
