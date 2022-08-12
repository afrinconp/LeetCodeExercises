"""1) Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
https://leetcode.com/problems/two-sum/"""
import timeit

class Solution:
    def __init__(self, List, name):
      self.num=List
      self.target=name
  
    def twoSum(self): #first solution, take more time
        Final=[0,0]
        for i in range(len(self.num)):
            for j in range(i+1,len(self.num)):
                if self.num[i]+self.num[j]==self.target:
                    if max(Final)<max([self.num[i],self.num[j]]) and  i!=j:
                      Final=[self.num[i],self.num[j]]
                      k,l=i,j
        return [k,l]
    
    def twoSum2(self): #second solution, take less time
        dic={}
        for i in range(len(self.num)):
          residuo=self.target-self.num[i]
          if residuo in dic:
            return [dic[residuo],i]
          dic[self.num[i]]=i
        
if __name__=="__main__":
    a=Solution([2,11,15,7,8,68],9)
    start = timeit.default_timer()
    print(a.twoSum())
    stop = timeit.default_timer()
    print("Time: ",stop-start)
    start = timeit.default_timer()
    print(a.twoSum2())
    stop = timeit.default_timer()
    print("Time: ",stop-start)
