## 2) Marking the test Cases

import pytest
def func(x):
	if x%2 == 0:
		return x+5
	else:
		return x-5

@pytest.mark.chouhan
def test_method():
	assert func(3)== 8
	
@pytest.mark.mohit
def test_method_2():
	assert func(2) == 7

@pytest.mark.mohit
def test_method3():
	assert 8 == 8
# -m flag is used to tell pytest 
# that we are going to use markers
# for selecting test cases.

# cmd: py.test -m mohit