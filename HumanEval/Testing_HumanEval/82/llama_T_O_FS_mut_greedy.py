def prime_length(string):
    
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True
assert prime_length("ABC") == True
assert prime_length("5") == False
assert prime_length("2*20") == False
