# unit test

import pytest
from cust_calc import *

def test_add():
    assert add(3, 4) == 7

def test_mul():
    assert mul(3, 4) == 12
    
def test_sub():
    assert sub(16, 8) == 8

def test_div():
    assert div(10, 5) == 2.0
