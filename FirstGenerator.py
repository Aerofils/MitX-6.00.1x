#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:06:58 2020

@author: Jo
"""


def genPrimes():
    Start = 1
    def is_prime_number(x):
        if x >= 2:
            for y in range(2,x):
                if not ( x % y ):
                    return False
        else:
	        return False
        return True

    while True:
        if is_prime_number(Start) == False:
            Start += 1
        else:
           next = Start
           yield next
           Start = next + 1
            
