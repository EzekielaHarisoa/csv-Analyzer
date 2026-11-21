from statistique import calculMedian
import csv
path = 'data/students.csv'

with open(path, mode="r",encoding="utf-8" ) as file:
   content = csv.DictReader(file)
   etudiant = list(content)
   
   i = 0
   #voir tout les contenue
   for f in etudiant:
      print("Etudiant:",f.get("nom"))
      i+=1
   print(f'nomre total detudiant {i}')
   
   print("\n")   

   #nom avec note
   for f2 in etudiant:
      print(f2.get("nom"),":" ,f2.get("note"))

   print("\n")   

   #type
   for f3 in etudiant:
      note = f3.get("note")
      print( note, " : ", type(note)) 


   listNotes = []
   for f5 in etudiant:
      note = float(f5.get("note"))
      listNotes.append(note)
   print(listNotes)   
   print( "mediane = ", calculMedian(listNotes))
   


