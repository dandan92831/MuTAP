def encrypt(s):
    
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 26]
        else:
            out += c
    return out


# test case
def test():
    assert encrypt("") == ""


    assert encrypt("a") == "a"


    assert encrypt("AbaCaDoEfGhIjKlMnOqRtUvWxyZ") == "LmNoRtUvWxyZ"


    assert encrypt("1234567890") == "NjMxMTAwOTMwMDAwMDAw"

def test_string_with_special_characters():
    s = "!@#$%^&*