collection = [1, 2, 5, 9, 11, 23, 7, 8, 1, 2, 51, 7, 8, 7, 8, 6, 7, 8 , 23, 0]

# 1. Faire la somme des 5 dernières valeurs de la liste collection.

sum( collection[-5::] )

# 2. Faire la somme des 5 premières valeurs de la liste collection.

sum( collection[:5] )

# 3. Faites une copie de la liste collection et ordonnez cette copie par ordre croissant. Puis faites la somme des valeurs entre l'indice 4 et 10.

collectionCopy = collection[:]

collectionCopy.sort()

sum(collectionCopy[4:10])

# 4. Faites la somme des valeurs une sur deux de la liste collection.

sum( collection[::2] )