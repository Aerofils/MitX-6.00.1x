#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:23:51 2020

@author: Jo
"""

def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    List = []
    for i in range(2,N+1):
        cutoff = i//2
        det = all([i%u!=0 for u in range (2,cutoff+1)])
        if det:
            List.append(i)
    return List