from plates import is_valid

def test_is_valid_num():
    assert is_valid("123") == False
    assert is_valid("TO23e3") == False

def test_is_valid_str():
    assert is_valid("hello") == True

def test_is_valid_len():
    assert is_valid("hello22222222") == False
    assert is_valid(" ") == False

def test_is_valid_alphanum():
    assert is_valid("ODD05") == False
    assert is_valid("Pi.98") == False
