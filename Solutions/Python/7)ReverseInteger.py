"""
7) Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range , then return 0.

https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    def __init__(self, x):
        self.x=x
    def reverse(self):
        string=str(self.x)
        reverso=string[::-1]
        if string[0]=="-":
            a=reverso[:len(string)-1]
            reverso=-1*int(a)
        else:
            reverso=int(reverso)
        if reverso >-2**31 and reverso <2**31-1:
            return reverso
        else:
            return 0
sol=Solution(-123123)
sol.reverse()
