# platform - leetcode
#link - https://leetcode.com/problems/maximum-subarray/description/
# concept -  finding the max subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        sum=0
        count=0
        k=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            if(sum>maxi):
                maxi=sum
                k=i
            if(sum<0):
                sum=0
        return maxi
         

        