
import pytest

TESTCASES = [
	(10, 5),  (10,2), (7,0), (10,3)
]

@pytest.mark.parametrize('a,b',TESTCASES)
def test_division(a, b):
	result = a / b
	assert b * result == a
