#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Jack Savage
# Student ID: 2295072 
# Email: jsavage@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018 Assignment: CW03
###

'''
MODULE DOCSTRING
'''
import math
import numpy as np

def s(a, n, T = 2*math.pi):
    '''
    Computes sum of equation given in readme
    
    Args:
        a (float): when multiplied by "T" gives "t" value used in equation
        n (int): term limit for sequence
        T (float): used in equation and in generating "t" value
    Returns:
        value (float): computed sum value
    '''
    # range of "k" values
    k = np.arange(1,n+1,1)
    t = a*T
    def compute_term(k, t, T = 2*math.pi):
        '''
        Computes the value of "k" using given function in readme
        
        Args:
            k (int/float): "k" value to be evaluated
            t (int/float): "t" value used in equation: defined in outer function
            T (float): "T" value used in equation: defined in outer function
            
        Returns:
            raw value (float): Value of function at "k"
        '''
        return (1/(2*k-1))*math.sin(((2*(2*k-1)*math.pi*t))/T)
        
    # evaluating function on domain array
    f = np.vectorize(compute_term)
    k = f(k,t)
    
    # multiplying sum of range array with constant to determine final vlaue
    value = (4/math.pi)*k.sum()
    return value

def f(t,T):
    '''
    Implementation of f(t) function given in readme
    
    Args:
        t (float): variable used in expression found in readme
    Returns:
        f(t) (int): function in readme evaluated at "t"
    '''
    if t == 0:
        return 0
    elif t < T/2 and t > 0.0:
        return 1
    elif t > -1*T/2 and t < 0.0:
        return -1
    else:
        return False