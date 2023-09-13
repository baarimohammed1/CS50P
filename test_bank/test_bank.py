from bank import value

def test_0():
    assert value("hello") == 0
def test_20():
    assert value("Hi!") == 20

def test_100():
    assert value("abcd123") == 100



