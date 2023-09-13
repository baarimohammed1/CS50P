import pytest
from twttr import shorten

def main():
    test_shorten_lower()
    test_shorten_upper()
    test_shorten_numbers()
    test_shorten_punc()

def test_shorten_lower():
    assert shorten("hello") == "hll"

def test_shorten_upper():
    assert shorten("HELLO") == "HLL"

def test_shorten_numbers():
    assert shorten("HELLO123") == "HLL123"

def test_shorten_punc():
    assert shorten("HELLO!") == "HLL!"

if __name__ == "__main__":
    main()
