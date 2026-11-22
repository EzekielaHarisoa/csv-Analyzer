
def exporterRapport(texte):
    with open("rapport.txt", mode="w", encoding="utf-8") as file:
        file.write(texte)

    print("Rapport exporté avec succès !")
