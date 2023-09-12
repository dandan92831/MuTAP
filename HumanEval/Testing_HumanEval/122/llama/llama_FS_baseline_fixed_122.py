def add_elements(arr, k):
    
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)


#</code>
#<test>

def test():
    assert add_elements([], 2) == 0
    assert add_elements([3, 4, 5, 5, 6], 2) == 7
