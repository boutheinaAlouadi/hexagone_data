
"""
Recherche d'une séquence donnée et de sa position

"""

collection = [1, 2, 5, 9, 11, 6, 7, 8, 1, 2, 6, 7, 6, 7, 8, 6, 7, 8 , 23, 0]

def search_word_pos(word, phrase):
    
    # On parcourt la chaîne en retirant la longueur de la chaîne recherchée pour ne pas sortir de la phrase
    for i in range(len(collection) - len(word)):

        j = 0
        # Pensez également à ne pas dépasser la longueur du mot ...
        while j < len(word) and collection[j + i] == word[j]:
            j += 1
        
        if j == len(word):
            return i

    return None

pos = search_word_pos([6, 7, 8], collection)

print(pos)