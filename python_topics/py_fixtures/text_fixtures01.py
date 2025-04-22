import pytest

@pytest.fixture()
def setup_list():
    print("\n in fixtures..\n")
    city = ['New York','London','Riyadh','Singapor','Mumbai']
    return city


def myRevese(lst):
    lst.reverse()
    return lst



def test_getlist(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'New York'
    assert setup_list[::2] == ['New York','Riyadh','Mumbai']



def test_reverseList(setup_list):
    assert setup_list[::-1] == myRevese(setup_list)

@pytest.mark.xfail(reason="usefixtures can't use the fixtures return valur")
@pytest.mark.usefixtures("setup_list")
def test_usefixturedemo():
    assert  1 == 1
    assert setup_list[0] == 'New York'
