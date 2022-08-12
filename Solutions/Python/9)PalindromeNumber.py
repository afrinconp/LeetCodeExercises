"""
9) Palindrome Number
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
https://leetcode.com/problems/palindrome-number/
"""

class Solution:
    def __init__(self,x):
        self.x=x  
    def isPalindrome(self):
        string=str(self.x)
        if string==string[::-1]:
            return True
        return False
u=Solution(121)
print(u.isPalindrome())
