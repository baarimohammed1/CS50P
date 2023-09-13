from um import count


def test_count():
    assert count("um") == 1
    assert count("sum") == 0
    assert count("Um") == 1