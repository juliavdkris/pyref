import pytest
from pyref import Ref


def test_int_ref_add():
	a = Ref(1)
	b = Ref(2)
	assert (a + b).value == 3
