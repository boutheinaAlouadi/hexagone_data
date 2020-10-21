# Introduction & revision Python

## Histoire & présentation

- Python est langage objet multi-paradigme. 

- Il est doté d’un typagedynamique fort. 

- C’est un langage libre. 

Ce langage peut s’adapter à tout type de contexte grâce à denombreux modules (extensions librairies). 

Il est très répendu dans le monde scientifique et notamment dans le calcul numérique (Data Analyste). Ce langage a été conçu par **Guido van Rossum**(Pays-Bas). Le début de ce langage commence pendant des vacances de Noël où le concepteur décide de travailler à sa création, fan des Monty Python il décide de baptiser son langage Python. 

- Le langage utilise l’indentation comme syntaxe.

## Structure de données

### Liste (structure de données)

Une liste est une suite de valeurs séparées par une virgule et placéesentre crochets. Considérons les exemples suivants.

Notion importante avant de commencer. Si vous copiez une liste dans une autre variable celle-ci sera référencée vers la même liste, elle n’est pas copiée. On notera également que les listes et les chaînes de caractères en Python ont des nombreuses propriétés en commun.


```python
l = [1,2,3,4,5,6,7]
m = l

# Même référence
m[0] = 100

print(l)
print(m)
```

- Exemples

```python
l = [1,2,3,4,5,6,7]
# accès valeur 1
l[0] 
# dernière valeur 7
l[-1] 

# slicing retourne une nouvelle liste [6,7]
l[-2:]

# copie de la liste précédente, a est une nouvelle liste
a = l[:]

```

Nous allons voir comment extraire des sous-listes d'une liste avec une méthode spécifique à Python : slicing.

```text
[start:stop:step]
```

- Exemples

```python

l = [1,2,3,4,5,6,7]

# affichera [2,3,4,5,6]
l[1:-1]

# affichera deux valeurs en partant du début [1,2]
l[:2]

# à partir de l'indice 2 jusqu'à la fin de la liste
l[2:]

#  début jusqu'à la fin en récupérant les éléments séparer de 2 indices
# affiche [1,3,5,7]
l[::2]

l = []
l.append(10)
# équivalent à l[len(l):] = [10]

# insert 100 à la position 2 donne [1, 2, 100, 3, 4, 5, 6, 7, 10]
l.insert(2, 100)

# pop dé-pile (élément retiré) de dernier élément d'une liste
l.pop() # 10

# retirer l'élément à l'indice 2 : 100
l.pop(2)

# supprime tous les éléments d'une liste équivalent à del l[:]
l.clear()

# renvoie le premier élément trouvé ou une exception de type ValueError, ici 2
l.index(3)

# compte le nombre d'élément 2 présent dans la lisye
l.count(2)

# longueur de la liste
len(l)

#  tri par ordre croissant
l.sort()

# tri par ordre décroissant avec une lambda fonction
l.sort(lambda x, y: x < y)
```

## Exercices sur les listes 

Soit la liste numbers suivantes :

```python
collection = [1, 2, 5, 9, 11, 23, 7, 8, 1, 2, 51, 7, 8, 7, 8, 6, 7, 8 , 23, 0]
```

1. Faire la somme des 5 dernières valeurs de la liste collection.

2. Faire la somme des 5 premières valeurs de la liste collection.

3. Faites une copie de la liste collection et ordonnez cette copie par ordre croissant. Puis faites la somme des valeurs entre l'indice 4 et 10.

4. Faites la somme des valeurs une sur deux de la liste collection.

## Exercices boucles

-  Boucle for en Python

```python
for i in [0, 1, 2, 3]:
    print("i a pour valeur", i)
```

- Avec une liste de valeurs de type string

```python
students = ["Alan", "Alice", "Bernard"]

for student in students;
    print(student)
```

En utilisant len, la fonction range de Python permet de générer une liste de valeurs numériques :

```python
students = ["Alan", "Alice", "Bernard"]

for i in range(len(students));
    print(students[i])
```

- Boucle while

```python
x = 1
while x < 10:
    print("Valeur de x", x)
    x = x * 2
print("End")

```

## Exercice répondre à une question sur une boucle

Avec un break, que fait à votre avis le code suivant ?

```python
while True:
    n = int(input("donnez un entier > 0 : "))
    print("votre choix", n)
    if n > 0:
        break
print("reponse correcte")
```

## Syntaxe instruction conditionnelle

```python
x = 15
if x > 10:
    print(x, "est plus grand que 10")
print("Fin")
```

- Avec un else

```python
x = 15
if x > 10:
    print(x, "est plus grand que 10")
else:
    print(x, "est plus petit que 10")
```

Pour les connecteurs on utilisera : or and.

## définition d'une fonction

Pour définir une fonction en Python on utilisera le mot def :

```python
def show(message):
    print(message)
```

## Exercice recherche d'une lettre dans une phrase

Notez qu'une chaîne de caractère peut se parcourir comme une liste.

Créez une fonction **search_letter** elle prendra deux paramètres : letter et phrase. Cette fonction retournera True ou False selon qu'elle aura trouvé ou non la lettre dans la phrase.

Notez qu'en Python les bolean s'écrivent : True et False

```python
s = 'mississippi'

search_letter('i', s) # True
```

## Exercice compte letter

Créez maintenant une fonction **count_letter** qui compte, dans une chaîne de caractères, le nombre de fois qu'une lettre donnée apparaît :

```python
s = 'mississippi'

count_letter('i', s) # 4
```

Si vous avez terminé cet exercice un autre exercice intéressant consiste à compter le nombre d'occurence de chaque caractères d'une phrase. Définissez cette fonction, vous l'appelerez **count_letters**. Pensez à la manière dont vous allez retourner votre recherche, vous pouvez par exemple utiliser une liste de liste comme suit :

```python
[ ['i', 4], ['m', 1], ['s', 4], ... ]
```

## Compréhension de liste 

Elles permettent la construction de liste de manière concise. 

- La compréhension de liste cubes génére une liste de 10 valeurs entières élevés au cube :

```python
cubes = [ x**3 for x in range(10) ]
```


## Exercices construction de points

Vous pouvez définir un tuple en Python pour représenter un vecteur : **(a, b)**. 

Voici deux listes l_A et l_B à l'aide d'une compréhension de liste générez une liste des points constitués des coordonnées X et Y :

```python
l_A = [1, 2, 3]
l_B = [4, 5, 6]
```

Liste de points attendus :

```python
coordintates = [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
```

Indications : vous pouvez faire une compréhension de liste dans une compréhension de liste.


## Dictionnaire

Les principales opérations sur les dictionnaires sont de stocker une valeur pour une clé et extraire la valeur correspondante pour une clé. 

On peut également supprimer une paire clé/valeur avec l’opérateur **del** de Python.

Attenion, si vous stockez une valeur pour une clé déjà présente dans le dictionnaire l’ancienne valeur sera perdue. 

Et si vous essayez d’accéder à une valeur pour une clé qui n’existepas une exception sera levée.


Un dictionnaire est un tableau de hash, ceci permet d’accéder à une valeur du dictionnaire en un temps constant et extrèmement rapide.

De même vérifier qu’une clé existe est directe.

- Exemples 

```python
students = {'alan' : 1, 'albert' : 2, 'brice' : 3}

print('albert' in students)

students = {'alan' : 1, 'albert' : 2, 'brice' : 3}

for h in map(hash, students):
    print(h)

# itération sur les valeurs
for student in students:
    print(student)

# itération sur les clés et les valeurs
for k,v in students.items():
    print(k,v)

# itération uniquement sur les clés
for k in students.keys():
    print(k)
```

## Tuples

Les tuples sont un autre type natif dit de séquence comme les listes et les dictionnaires, les tuples sont non modifiables (non mutable),ils n’ont pas de méthode. Un tuple est donc protégé en écriture. 

C’est un tableau de hash donc rapide pour l’accès et le parcours de ses éléments. 

Comme il est non mutable on peut l’utiliser comme clé d’un dictionnaire par exemple. On rappelle qu’une clé d’un dictionnaire doit être non mutable

```python
a = (3, 4, 7)

a[0]

# unpacking
u, v, w = a
```