## Way of Selecting or filtering 
## test cases
# 1) Running the test cases with
# substring matching approach

import pytest

def func(x):
	if x%2 == 0:
		return x+5
	else:
		return x-5

def test_func1():
	assert func(3)== 8

def test_func2():
	assert func(2) == 7

def test_method3():
	assert 8 == 8

# we pass substring to match by
# -k flag
# cmd: py.test -k test_func