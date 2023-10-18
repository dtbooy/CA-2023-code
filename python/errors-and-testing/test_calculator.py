import calculator
import pytest

def test_add():
    assert calculator.add(5 , 3) == 8
    assert calculator.add(-5 , 3) == -2
    assert calculator.add(5 , 3.2) == 8.2


# To test for errors
def test_divide_by_zero():
    with pytest.raises(Exception):
        calculator.divide(10, 0)
    
# testing user inputs is called monkey patching - not covered in lesson - look up later
