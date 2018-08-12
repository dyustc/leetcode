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

OPENING_BRACKETS = {"{", "[", "("}
BRACKETS_MAP = {"]": "[", "}": "{", ")": "("}

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """  
        '''
        i = 0
        length = len(s)
        while i < length / 2:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
            if s == '':
                return True
            i += 1
            
        return False
        '''
        if not s:  # empty string is a valid string
            return True

        if s[0] not in OPENING_BRACKETS:
            return False  # early exit if string does not start with an opening bracket

        stack = []
        for index, bracket in enumerate(s):
            if bracket in OPENING_BRACKETS:
                stack.append(bracket)
            else:
                try:
                    last_opening_bracket = stack.pop()
                    if last_opening_bracket != BRACKETS_MAP[bracket]:  # last closing bracket does not match last opening bracket
                        return False
                except IndexError:
                    return False  # pop from an empty stack means the brackets are not balanced

        return not stack  # if something left on stack, brackets are unbalanced
        
            


solution = Solution()
example = "{[]}"
print(solution.isValid(example))
                    