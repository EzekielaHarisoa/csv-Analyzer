
def calculMedian(x):
    x.sort()
    n = len(x)

    if n % 2 != 0:
        return  x[n// 2] 
    else:
        m1 = n // 2
        m2 = n // 2  - 1

        mediane = (x[m1] + x[m2]) / 2

        return  mediane

def calculMoyenne(x):
    sommeValeur = sum(x)
    nbrValeur = len(x)
    moyenne = sommeValeur/nbrValeur

    return moyenne

def calculMin(x):
    return min(x)

def calculMax(x):
    return max(x)

def calculEtendu(x):
    return max(x) - min(x)

def calcluNbreNote(x):
    return len(x)

def calculSomme(x):
    return sum(x)

def netoyerNote(x):
    valideNote=[]
    for valeur in x:
        try :
            note = float(valeur)

            if 0 <= note <=20:
                valideNote.append(note)

        except(ValueError, TypeError):
            continue

    return valideNote            

def compterCategories(x):
    effectif = {}
    for valeur in x:
        valeur = valeur.strip()

        if valeur == "":
            continue
        if valeur in effectif:
            effectif[valeur] += 1
        else:
            effectif[valeur] = 1    
    return effectif    

