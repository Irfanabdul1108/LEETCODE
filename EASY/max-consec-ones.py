# platform - leetcode
#link - https://leetcode.com/problems/max-consecutive-ones/description/
# concept - return the maximum number of consecutive 1's in the array. 

 
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum=0
        maxi=0
        for i in range(len(nums)):
            if(nums[i]==0):
                sum=0
            else:
                sum=sum+nums[i]
                if(sum>maxi):
                    maxi=sum
        return maxi
        