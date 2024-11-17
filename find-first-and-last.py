# platform - leetcode
#link -  https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# concept - sorting


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        list2=[-1,-1]
        def first(nums, target,req):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if req=='f' and nums[mid] == target:
                    list2[0]=mid 
                    right = mid - 1  
                elif req=='s' and nums[mid] == target:
                    list2[1]=mid   
                    left = mid + 1  
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        first(nums, target,'f')  
        first(nums, target,'s')  
        return list2