asd = 'qwertyuiopasdfghjklzxcvbnm'
def count_upper(w):
    count = 0
    for l in w:
        for a in asd:
            if l == a:
                count += 1

    return count
def count_lower (w):
    count = 0 
    for l in w:
        for a in asd:
            if l == a:
                count += 1
    return count
sen = 'qwertt'
print('qwertty{count_upper( sen)}')
        
        
    


