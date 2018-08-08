#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 12:46:03 2018

@author: daiyi02
"""

'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        single = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        double = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        
        
        for i in double:
            dict[i] = 0 
            if i in s:
                dict[i] = 1
                s = s.replace(i, '')
        
        for i in single:
            dict[i] = 0
        
        for i in s:
            dict[i] += 1
        
        #print(dict)
        
        return dict['IV'] * 4 + dict['IX'] * 9 + dict['XL'] * 40 + dict['XC'] * 90 + dict['CD'] * 400 \
            + dict['CM'] * 900 + dict['I'] * 1 + dict['V'] * 5 + dict['X'] * 10 + dict['L'] * 50 \
            + dict['C'] * 100 + dict['D'] * 500 + dict['M'] * 1000
        

solution = Solution()
example = 'MIV'

print(solution.romanToInt(example))
        
            