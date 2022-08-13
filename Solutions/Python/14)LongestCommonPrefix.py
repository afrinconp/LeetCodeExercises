"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefijo=""
        palabra=""
        if len(strs)==0:
            return prefijo
        strs.sort(key=len)
        uno=strs[0]
        semaforo="verde"
        union=""
        for i in range(len(uno)):
            j=0
            while j <len(strs) and semaforo=="verde":
                if uno[i] == strs[j][i]:
                    palabra=uno[i]
                else:
                    semaforo="rojo"
                j=j+1
            if semaforo=="rojo":
                break
            union+=palabra
            if len(prefijo)<len(union):
                prefijo=union
            semaforo="verde"
        return prefijo
