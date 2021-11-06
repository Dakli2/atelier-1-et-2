n=int(input('entrer un nombre '));
somme=0 ;
def sum ( n ) :
 global somme# variable local
 if n == 0:# l'elément d'arrét
  return  0
 else :
   sum(n //10) # division de n a 10 jusqu'a quand n=0
   somme = somme + 1 # incrémenter somme a chaque division
 return somme
print('le nombre des chifre dans ce nombre est :' + str(sum(n)))