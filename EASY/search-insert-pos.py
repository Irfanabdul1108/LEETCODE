# platform - leetcode
#link -  https://leetcode.com/problems/search-insert-position/
# concept - finding the correct position  where the element could be present in the array
    
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                right=mid-1
            else:
                left=mid+1
        return left
            
        