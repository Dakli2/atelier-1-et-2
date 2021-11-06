n=int(input('enter le nombre '))
def somme(n):
  if n== 0 : # element d'arrét 1
   return 0
  elif n==1 : # element d'arrét 2
   return 1
  else :
   return somme(n-2)+somme(n-1) # effectuer le calcul par appel du fct somme
print('la serie de fibonchi en terme ', str(n) , 'est:' )
for i in range(n) : # boucle pour calcul a chaque i somme(i)
 print(somme(i))