import pytest

def test_case01():
    with pytest.raises(AssertionError):
        #assert (1/0)
        assert 3 < 2

def func():
    raise ValueError("exception func raised")

def test_case02():
    with pytest.raises(Exception) as excnfo:
        #assert (1,2,3) == (1,2,4)
        func()
    print(str(excnfo))