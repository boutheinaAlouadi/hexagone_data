collection = [1, 2, 5, 9, 11, 6, 7, 8, 1, 2, 6, 7, 6, 7, 8, 6, 7, 8 , 23, 0]

def search_letter(letter, phrase):
    search = []
    
    for l in phrase:
        if l == letter:
            search.append(l)
            return search
        
    return search

print( search_letter(2, collection)  )

def search_letter_pos(letter, phrase):
    search = []
    
    for i, l in enumerate(phrase):
        if l == letter:
            # avec un dictionnaire { pos : pos, val : l }
            search.append((i, l) )
            return search
        
    return search

print( search_letter_pos(2, collection) )

# Ce code marcherait également sur une chaîne de caractères

phrase = "bonjour tout le monde"
print ( search_letter_pos("b", phrase)  ) 
