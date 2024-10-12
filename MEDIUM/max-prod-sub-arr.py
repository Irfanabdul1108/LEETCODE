# platform - leetcode
#link - https://leetcode.com/problems/maximum-product-subarray/description/
# concept -  finding maximum product subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref=1
        maxi=float('-inf')
        suff=1
        for i in range(len(nums)):
            if pref==0:
                pref=1
            if suff==0:
                suff=1
            pref=pref*nums[i]
            suff=suff*nums[len(nums)-i-1]
            maxi=max(maxi,max(pref,suff))
        return maxi
