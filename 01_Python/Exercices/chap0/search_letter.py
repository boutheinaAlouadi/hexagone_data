message = 'mississippi'

def search_letter(letter, message):

    for ch in message:
        if ch == letter:
            return True 
    
    return False