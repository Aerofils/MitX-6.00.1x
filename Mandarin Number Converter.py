#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:49:01 2020

@author: Jo
"""


def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    
    if len(us_num) == 1:
        return trans[us_num]
    elif us_num[0] == '1':
        if us_num[1] == '0':
            return trans[us_num]
        else:
            return trans['10']+' '+trans[us_num[1]]
    else:
        if us_num[1]=='0':
            return trans[us_num[0]]+' '+trans['10']
        else:
            return trans[us_num[0]]+' '+trans['10']+' '+trans[us_num[1]]
    
for i in range(21):
    print(convert_to_mandarin(str(i)))
        