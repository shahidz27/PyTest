import pytest

weekdays1 =  ['mon','tue','wed']
weekdays2 = ['fri','sat','sun']



@pytest.fixture()
def setup01():
    wk1 = weekdays1.copy()
    wk1.append('thur')
    yield wk1
    print("\n after yield \n")
    wk1.pop()
    print(wk1)

def test_extendList(setup01):
    setup01.extend(weekdays2)
    assert setup01 == ['mon','tue','wed','thur','fri','sat','sun']