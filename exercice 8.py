nom = input('enter une chaine de caractere ') # decalaration du chaine de caractere
caractere = input('enter le caractere a rechercher') # declaration du caractere
f = 0 # initialisation du frequenceb par zero --- somme carrecte
for i in range(0, len(nom), 1):
 if nom[i] == caractere:
  f = f+1 # incrémenter du f si on trouve le caractere
print('frequence de ce caractere est ', f) # affiche du nombre d'ocurence c'est f