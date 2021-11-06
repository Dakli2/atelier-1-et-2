n=int(input('entrer un nombre decimal')); # variale global
def convertir(n) :
 if n==0 : # element d'arrét
  return 0
 else :
  convertir(int(n/2)) # appel a la fonction lui méme
  print(n%2 , end="" ) # end "" pou afficher a le meme ligne
print('le nombre en binaire est :')
convertir(n) # affiche le nombre binnaire du n par recusivité