#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 15:26:24 2018

@author: daiyi02
"""
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        right = [')', ']', '}']
        if s == '':
            return True
        elif s[0] in right:
            return False
        elif ')' not in s and ']' not in s and '}' not in s:
            return False
        else:
            length = len(s)
            print(length)
            for i in range(length):
                if s[i] in right:
                    if s[i-1:i+1] not in ['()', '[]', '{}']:
                        return False
                    else:
                        print(s[i-1:i+1])
                        s = s.strip(s[i-1:i+1])
                        print(s)
                        return self.isValid(s)




solution = Solution()
example = "{[]}"
print(solution.isValid(example))
                    