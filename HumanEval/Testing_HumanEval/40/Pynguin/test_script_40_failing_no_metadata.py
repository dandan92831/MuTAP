# Automatically generated by Pynguin.
import script_40 as module_0


def test_case_0():
    try:
        bool_0 = False
        list_0 = [bool_0]
        var_0 = module_0.triples_sum_to_zero(list_0)
        assert var_0 is False
        list_1 = [bool_0, bool_0, bool_0, bool_0]
        var_1 = module_0.triples_sum_to_zero(list_1)
        assert var_1 is True
        list_2 = [bool_0, bool_0]
        var_2 = module_0.triples_sum_to_zero(list_1)
        assert var_2 is True
        list_3 = [var_2, list_2, var_0]
        var_3 = module_0.triples_sum_to_zero(list_3)
    except BaseException:
        pass
