# platform - leetcode
#link - https://leetcode.com/problems/binary-search/description/
# concept - find an element in the array with t.comp - o(logn)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1 
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

        
