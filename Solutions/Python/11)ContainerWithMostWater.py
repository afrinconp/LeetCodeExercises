
"""
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


class Solution: #It takes more time (It could be Time Limit Exceeded)
    def maxArea(self, height: List[int]) -> int:
        maxarea=0
        for i,j in enumerate(height):
            k=i
            while k<len(height):
                width=k-i
                area=width*min(j,height[k])
                if area>maxarea:
                    maxarea=area
                k+=1
        return maxarea
        
class Solution: #It takes less time
    def maxArea(self, height: List[int]) -> int:
        derecha=len(height)-1
        izquierda=0
        maxarea=0
        while derecha>izquierda:
            ancho=derecha-izquierda
            maxarea=max(min(height[derecha],height[izquierda])*ancho,maxarea)
            if height[derecha]>height[izquierda]:
                izquierda+=1
            else: derecha-=1
        return maxarea
