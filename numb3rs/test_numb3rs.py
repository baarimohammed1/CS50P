from numb3rs import validate

def test_validate():
    assert validate("123.123.123.123") == True
    assert validate("523.123.123.123") == False
    assert validate("123.523.123.123") == False
    assert validate("123.123.523.123") == False
    assert validate("123.123.123.523") == False
    assert validate("cat") == False
    assert validate("") == False