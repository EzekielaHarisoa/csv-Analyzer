from statistique import calculEtendu, calculMax, calculMedian, calculMin, calculMoyenne, calculSomme, netoyerNote


def analyserNotes(x):
     notevalide = netoyerNote(x)
     if len(notevalide) == 0:
          return None
     resultat = {
          "moyenne" : calculMoyenne(notevalide),
          "somme": calculSomme(notevalide),
          "moyenne": calculMoyenne(notevalide),
          "minimum": calculMin(notevalide),
          "maximum": calculMax(notevalide),
          "etendue": calculEtendu(notevalide),
          "mediane": calculMedian(notevalide)
     }
     return resultat