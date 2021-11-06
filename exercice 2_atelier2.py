list=[1,2,11,44,7,8,5,11,9]
list1=[]
list2=[]
list3=[]
for i in range (0,int(len(list)/3) , 1):
 list1.append(list[i]) # remlir premier list par 1/3 du list
for i in range (int(len(list)/3) ,int(len(list)/3)+3 , 1):
 list2.append(list[i]) # remlir premier list par 2/3 du list
for i in range(int(len(list)/3)+3 , len(list) , 1) : # remplir du list3 par le reste du list
 list3.append(list[i])
print("avant d'inverser") # affichage des listes avnt l'operation
print("list 1  :")
print(list1)
print('\n')
print("list 2 : ")
print(list2)
print('\n')
print("list 3 :")
print(list3)
print('\n')
print("apres operation")  # affichage des listes apres l'operation d'inversement
print("list 1  :")
print('[',end="")
for i in range (len(list1) , 0 ,-1):
 print(list1[i-1],',', end="")
print(']')
print('\n')
print("list 2  :")
print('[',end="")
for i in range(len(list2), 0, -1):
 print(list2[i-1],',', end="") # end="" pour mettre la list a un seul ligne
print(']')
print('\n')
print("list 3  :")
print('[',end="")
for i in range(len(list3), 0, -1):
 print(list3[i-1],',', end="")
print(']')
print('\n')
