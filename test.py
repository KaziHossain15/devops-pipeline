from operator import add, sub as subtract, mul as multiply, truediv as divide  # noqa: F401


def test_add():
    assert add(1, 1) == 2

def test_subtraction():
    assert subtract(2, 1) == 1

def test_mult():
    assert multiply(2, 3) == 6

def test_div():
    assert divide(6, 3) == 2