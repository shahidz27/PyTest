
import pytest
pytestmark = [pytest.mark.smoke,pytest.mark.strtest]


def test_str01():
    num = 9/4
    s1 = 'I like ' + 'python automation'
    assert str(num) == '2.25'
    assert s1 == 'I like python automation'
    assert s1 + str(num) == 'I like python automation2.25'
@pytest.mark.sanity
@pytest.mark.str
def test_str02():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert len(letters) == 26

@pytest.mark.sanity
def test_str03():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[0] == 'a'
    assert letters[-1] == 'z' == letters[25]