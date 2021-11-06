n=int(input('enter le nombre '))
def somme(n):
 if n == 0: # element d'arrét
  return 0
 else:
  return (n + somme(n - 1)) # fait apel somme(n) piur affectuer le calcul
print('la somme de 1 à ',str(n) , 'est ', str(somme(n))) # affiche du somme