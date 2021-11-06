n=int(input('entrer le nombre de la serie' )) #declaration de un variable  entier c'est le terme du serie
sum=0 # initialisation du sum par zero pour avoir un somme juste
fact=1 # initialisation du factoriel par zero pour avoir une multiplication  juste
for i in range(1,n+1): #boucle de 1 a n+1
 fact=fact*i # a chaque i on calcul son factoriel
 sum+= fact/ i # on effectue la somme du facto sur son nombre
print( 'somme est ' +str(sum)) # on affiche le resultat du somme de n