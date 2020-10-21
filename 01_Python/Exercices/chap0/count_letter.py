message = 'mississippi'

def count_letter(letter, message):
    count = 0

    for ch in message:
        if ch == letter:
            count += 1 
    
    return count

count_letter('i', message)