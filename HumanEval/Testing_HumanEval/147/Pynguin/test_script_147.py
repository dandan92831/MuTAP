# Automatically generated by Pynguin.


import script_147 as module_0


def test_case_0():
    bool_0 = True
    var_0 = module_0.get_max_triples(bool_0)
    assert var_0 == 0


def test_case_1():
    int_0 = 8
    var_0 = module_0.get_max_triples(int_0)
    assert var_0 == 11
    bool_0 = True
    var_1 = module_0.get_max_triples(bool_0)
    assert var_1 == 0
    var_2 = module_0.get_max_triples(var_0)
    assert var_2 == 39
    var_3 = module_0.get_max_triples(var_2)
    assert var_3 == 2886
    
    
