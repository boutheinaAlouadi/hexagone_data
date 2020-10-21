# Introduction à Python et concept d'analyse des données

Dans ce chapitre d'introduction à Python nous allons utiliser les listes, structure de données, en Python et des fonctions. Ouvrez le notebook du cours pour le cours et exercices. Vous pouvez faire les exercices dans un fichier à part et les importez également dans le notebook. Nous verrons cela de manière pratique dans le cours.

- Une liste est une structure de données en Python, elle se définie à l'aide de crochet ouvrant/fermant et peut contenir tout type de valeur.

```python
collection = [1, 2, 3, 4, 5, 6]
```

Chaque élément d'une liste est atteignable à l'aide de son indice :

```python
# affiche 2
print(collection[1])
```

Pour ajoutez une valeur à la fin d'une liste vous utiliserez la méthode append :

```python
# affiche 2
collection.append(19)
```

- une fonction en Python se définie à l'aide du mot clé def. Notez qu'en python il n'y a pas de point-virgule ou délimiteur pour terminer une instruction ou entrer dans un bloc de code (boucle, fonction, ...). Python utilise l'indentation, les retraits vers la droites doivent être identiques pour un bloc donné, et les ":" définissent l'entrée du bloc.

*Remarque : Pour écrire des commentaires dans votre code vous utiliserez le dièse ou les triples cotes :*

```python
# Un commentaire

"""
Un commentaire plus long
sur plusieurs lignes
"""
```

```python
def search_word(word, phrase):
    
    result = "#".join( phrase.split(' '))

    # f pour faire de l'interpolation {} permet d'interpréter les variables
    return f"Vous chercher le mot {word} dans l'ensemble de mots : {result}"

search_word('python', 'Découvrons le langage Python')
```

## Exercice recherche d'une occurence et de sa position

Pour parcourir une collection vous utiliserez une boucle for, ci-dessous on parcourt la liste collection et on affiche dans la boucle chacune des ses valeurs à l'aide du mot réservé print de Python :

```python
collection = [1, 2, 3, 4, 5, 6]

# letter est une variable de votre choix
for letter in collection:
    print(letter)
```

Pour les conditions vous utiliserez la syntaxe suivante :

```python
# code ...

if letter == 'e':
    print(f"find {e}")
```

*Remarque le print ci-dessus utilise la syntaxe format pour interpréter les valeurs dans une chaîne de caractères.*

```python
d = 1789
f"Date de la révolution {d}"
# 'Date de la révolution 1789'
```

1. Soit la liste collection suivante créez une fonction **search_letter**, elle retournera une liste avec le premier mot (nombre) recherché, ou une liste vide si elle n'a rien trouvé.

```python
collection = [1, 2, 5, 9, 11, 6, 7, 8, 1, 2, 6, 7, 6, 7, 8, 6, 7, 8 , 23, 0]
```

2. Améloriez cette fonction en donnant la position du premier élément rechercher dans la liste. Utilisez la fonction enumerate sur la liste collection elle-même pour avoir l'indice de chaque lettre. Voyez l'exemple qui suit pour enumerate :

```python
collection = [1, 2, 3, 4, 5, 6]

# letter est une variable de votre choix
for pos, letter in enumerate( collection ):
    print(letter)
```

Pour récupérer la position et la valeur de l'élément dans la liste utilisez la structure de données tuple de Python :

```python
coordinate = (1, 2) # (pos, val)
```

On peut également utiliser un dictionnaire pour récupérer cette information :

```python
search = { 'pos' : 1, 'val' : 2 }
```

### Exercice recherche de toute(s) les occurences d'un mot dans une phrase

Reprenez la collection ci-dessus et recherchez maintenant toute les occurences d'une lettre donnée dans la collection.

Pour récupérer ces informations utiliser la structure de données suivante :

```python
result = {'letter': 7, 'pos': [6, 11, 13, 16]}
```

Rappel : pour accéder/modifier à une valeur d'un dictionnaire :

```python
result['letter']
result['letter'] = "Six"
```

### Recherche d'une séquence ou des séquences dans une phrase

Cet exercice est un peu plus difficile que les autres ...

Remarque : vous pouvez utiliser la fonction range de Python, elle génère une liste de valeur(s) numériques. L'exemple suivant affichera les valeurs de 0 à 9 : 

```python
# 0 <= i < 10
for i in range(10):
    print(i)
```

Si vous souhaitez également utiliser une boucle while voici un exemple de syntaxe en Python, la fonction Python len retourne la longueur de la chaîne :

```python
j = 0
while j < len(word):
    j += 1
```

1. Reprennez la collection précédente et rechercher maintenant si une séquence particulière est présente dans une phrase, par exemple 6, 7, 8 est une séquence présente dans la liste collection. La fonction retournera la position de la première séquence trouvée ou None (valeur Python).

2. Reprennez l'exercice précédent et créez maintenant une fonction trouve toutes les séquences d'une phrase et renvoie le premier indice de chaque séquence trouvée.

