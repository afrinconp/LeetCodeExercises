"""
15) 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

https://leetcode.com/problems/3sum/

"""
class Solution:
    def threeSum(self, nums) -> list():
        nums.sort()
        resultado=[]
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            r,l=0,1
            while len(nums)-r-1>i+l:
                if a+nums[i+l]+nums[len(nums)-r-1]==0:
                    resultado.append([a,nums[i+l],nums[len(nums)-r-1]])
                    l+=1
                    while nums[i+l-1]==nums[i+l] and i+l<len(nums)-r-1:
                        l+=1
                        
                elif nums[i]+nums[i+l]+nums[len(nums)-r-1]>0:
                    r+=1
                elif nums[i]+nums[i+l]+nums[len(nums)-r-1]<0:
                    l+=1
        return resultado
sol=Solution()
sol.threeSum([-1,0,1,2,-1,-4])
