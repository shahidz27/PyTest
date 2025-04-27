import pytest

months = ["jan","feb","mar"]
def test_checkrequest(setup04):
    assert 1==1
    assert "april" in setup04
    assert len(setup04) == 4

def test_fat_fixture(setup05):
    assert type(setup05('list')) == list
    assert type(setup05('tuple')) == tuple
