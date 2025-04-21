
import sys
import pytest
#pytestmark = pytest.mark.skipif(sys.platform == 'win32',reason="will only work on linux")

const = 9 / 5
def cent_to_fah(cent = 0):
    fah = (cent * const) + 32
    return fah
#print(cent_to_fah())


@pytest.mark.skip(reason="skipping for fun")
def test_case01():
    assert type(const) == float

#@pytest.mark.skipif(sys.version_info > (3,8), reason="does not work on py version > 3.8")
#@pytest.mark.skipif(cent_to_fah() == 32,reason = "default value test, so skipping")
def test_case02():
    assert cent_to_fah() == 32

@pytest.mark.skipif(pytest.__version__ > '5.4.0',reason="pytest version is greater")
def test_case03():
    assert cent_to_fah(38) == 100.4
