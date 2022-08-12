"""
8) String to Integer (atoi)
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.

Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.

Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.

Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
https://leetcode.com/problems/string-to-integer-atoi/
"""

class Solution: #Solution1
    def myAtoi(self, s: str) -> int:
        #Generates all the digit numbers
        digits=list(map(lambda x: str(x), range(10)))
        s=s.strip()
        new=''
        #When the string is empty
        if len(s)<=0:
                return 0
        if s[0] in ['+','-'] and len(s)==1:
            return 0
            
        #Going through the index of the string
        for i in range(len(s)):
            if s[i] in ['+','-']:
                if len(new)==0 and s[i+1] in digits:
                    new=new+s[i]
                elif len(new)>0:
                    break
                else:
                    return 0
            elif s[i] in digits:
                new=new+s[i]
            else:
                if len(new)>0:
                    break
                else:
                    return 0
        new_int=int(new)
        if new_int < -2**31:
            new_int=-2**31
        if new_int > 2**31-1:
            new_int=2**31-1
            
        return new_int

sol1=Solution()
sol1.myAtoi('+44+')

#Code 2
class Solution2: #Solution2
    def myAtoi(self, s: str) -> int:
        numeros =["1","2","3","4","5","6","7","8","9","0"]
        nuevo=""
        for i in range(len(s)):
            if s[i]==" ":
                if len(nuevo)>0:
                    return int(nuevo)    
            elif s[i]=="+" or s[i] =="-":
                if i==len(s)-1:
                    break
                if s[i+1] in numeros:
                    nuevo+=s[i]
                else:
                    return 0
            elif s[i] in numeros:
                    nuevo+=s[i]
                    if i==len(s)-1:
                        break
                    if s[i+1] not in numeros:
                        break
            else:
                break
        if len(nuevo)==0:
            return 0
        else:
            entero=int(nuevo)
            if entero>=2**31:
                return 2**31-1
            elif entero<-2**31:
                return -2**31
            else:
                return entero
sol2=Solution()
sol2.myAtoi('+44+')
