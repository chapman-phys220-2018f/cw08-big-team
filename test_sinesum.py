#!/usr/bin/env python3

"""sinesum.py Test Module

Verify implementation of the Fourier sine series using numpy arrays.
"""

import sinesum
import math

def test_s():
    """With given inputs, "s" function should equal sin(1)"""
    assert math.isclose((sinesum.s(1/(2*math.pi),1)/(4/math.pi)), math.sin(1)), "s function not working properly"

def test_f():
    """Ensures each use case is working correctly"""
    assert sinesum.f(1) == 1, "Not working for cases > 0"
    assert sinesum.f(-1) == -1, "Not working for cases < 0"
    assert sinesum.f(0) == 0, "Not working for t = 0"