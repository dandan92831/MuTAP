# Automatically generated by Pynguin.
import script_26 as module_0


def test_case_0():
    int_0 = 538
    list_0 = [int_0]
    list_1 = module_0.remove_duplicates(list_0)
    assert list_1 == [538]



def test_case_1():
    int_0 = -551
    int_1 = 93
    list_0 = [int_0, int_1, int_1, int_1]
    list_1 = module_0.remove_duplicates(list_0)
    assert list_1 == [-551]

