import sys

import pytest


def test_strjoin():
    s1 = 'python,Pytest and Automation'
    l1 =['python,Pytest', 'and', 'Automation']
    l2 =['Python', 'Pytest and Automation']
    assert ' '.join(l1) == s1

@pytest.mark.xfail(raises=IndexError,reason="issue")
def test_str04():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[100]

@pytest.mark.xfail(sys.platform == "win32",reason="only works on windows")
def test_str05():
    letters = 'abcd'
    num = 1234
    assert letters + num == 'abcd1234'
