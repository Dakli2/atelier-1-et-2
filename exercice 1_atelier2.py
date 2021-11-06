list11 = [1, 2, 3, 4, 5, 6]
list12 = [7, 2, 1, 14, 5, 16,8]
list3 = []
list4 = []
for i in range(0, len(list11), 1):# remplir le deuxieme list par les elemnts d'indice impaire de liste11
 if i % 2 != 0:
  list3.append(i+1)
for i in range(0, len(list12), 1):
      if i % 2 == 0:  # remplir le premier list par les elemnts d'indice paire de liste12
          list4.append(list12[i])
result= list3+list4 # concaténer les deux listes pour avoir resultat
print(result)