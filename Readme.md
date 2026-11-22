# CSV Analyzer

CSV Analyzer est un petit projet Python permettant de lire et d'analyser des données provenant d'un fichier CSV.

## Fonctionnalités

- Analyse statistique des notes (moyenne, médiane, minimum, maximum et étendue).
- Analyse des catégories et calcul des pourcentages.
- Détection des valeurs manquantes.
- Détection des doublons.
- Filtrage des étudiants par ville.
- Exportation des résultats dans un fichier TXT.

## Technologies utilisées

- Python
- CSV

## Installation

1. Cloner le projet :

```bash
git clone URL_DU_DEPOT
```

2. Entrer dans le dossier :

```bash
cd csv-analyzer
```

3. Lancer le programme :

```bash
python main.py
```

## Structure du projet

```text
csv-analyzer/
├── data/
│   └── students.csv
├── main.py
├── affichage.py
├── statistique.py
├── netoyage.py
├── rapport.py
├── README.md
└── .gitignore
```

## Objectif

Ce projet a été réalisé dans le cadre de mon apprentissage de Python et de l'analyse de données.