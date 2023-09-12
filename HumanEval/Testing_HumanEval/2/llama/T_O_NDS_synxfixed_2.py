def truncate_number(number: float) -> float:
    
    return number % 1.0




# test case
def test():
    # Test with positive numbers
    assert truncate_number(1.0) == 1.0
    assert truncate_number(2.0) == 2.0
    assert truncate_number(3.0) == 3.0
    # Test with negative numbers
    assert truncate_number(-1.0) == -1.0
    assert truncate_number(-2.0) == -2.0
    assert truncate_number(-3.0) == -3.0
    # Test with very large and very small numbers
    assert truncate_number(1e10) == 1.0
    assert truncate_number(1e-10) == 1.0
    # Test with rounding errors
    assert truncate_number(1.0 + 0.0000000001) == 1.0
    assert truncate_number(1e10) == 1.0