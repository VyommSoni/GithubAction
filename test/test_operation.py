from src.math_operation import add,substract

def test_add():
    assert add (2,3)==5
    assert add(-1,1)==0
    assert add (5,3)==8


def test_substract():
    assert substract(5,3)==2
    assert substract(4,3)==1
    assert substract(3,3)==0

    