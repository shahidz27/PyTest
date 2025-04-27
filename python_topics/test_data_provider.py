import pytest
from python_topics.utils.util import get_data

@pytest.mark.parametrize("a,b,c,d",get_data())
def test_checkdata(a,b,c,d):
    print(a)