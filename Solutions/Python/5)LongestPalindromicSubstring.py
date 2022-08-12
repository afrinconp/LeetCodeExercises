"""
5) Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

https://leetcode.com/problems/longest-palindromic-substring/solution/
"""
def polidromic(s):
        final_str=""
        prueba_lista=""
        for k in range(len(s)):
            r,l=0,0
            while k-l>=0 and len(s)>k+r and s[k-l]==s[k+r]:
                prueba_lista=s[k-l:k+r+1]
                l,r=l+1,r+1
                if len(prueba_lista)> len(final_str):
                    final_str=prueba_lista
            r,l=1,0
            while k-l>=0 and len(s)>k+r and s[k-l]==s[k+r]:
                prueba_lista=s[k-l:k+r+1]
                l,r=l+1,r+1
                if len(prueba_lista)> len(final_str):
                    final_str=prueba_lista         
        return final_str
polidromic("babad")
