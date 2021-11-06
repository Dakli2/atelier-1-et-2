tableau =['57' ,'2', '5', '7']
#tri par insertion decroissante < >
#on suppose que le max de ce tableau est tab[0]
max =tableau[0] # initialisation du max par premier element
for i in range(0, len(tableau)-1 , 1) :
 if max < tableau[i+1] :
  max = tableau[i+1]
  tableau[i+1]= tableau[i]
  tableau[i]=max
#affichage du tableau trie
for i in range(0 ,len(tableau)-1 , 1):
 print(tableau[i+1])