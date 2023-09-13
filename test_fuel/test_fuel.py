from fuel import convert
from fuel import gauge
import pytest


def test_convert():
    assert convert("7/10") == 70
    with pytest.raises(ZeroDivisionError):
        convert("7/0")



def test_guage():
    assert gauge(56) == "56%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
