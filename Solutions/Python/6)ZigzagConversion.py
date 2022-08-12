"""
6) Zigzag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P  A  H  N

A P L S  I  I  G

Y  I  R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

https://leetcode.com/problems/zigzag-conversion/
"""

def convert(s, numRows):
  resultado=""
  for j in range(numRows):
    if j != numRows-1 and j !=0:
      posicion=j
      while posicion <len(s):
        resultado+=s[posicion]
        posicion+=2*(numRows-j-1)
        if posicion <len(s):
          resultado+=s[posicion]
          posicion +=2*j
    else:
      if numRows>1:
        posicion=j
        while posicion <len(s):
          resultado+=s[posicion]
          posicion+=2*(numRows-1)
      else:
        return s
  return resultado
a=convert("PAYPALISHIRING",3)
print(a)
