# platform - leetcode
#link - https://leetcode.com/problems/contains-duplicate/description/
# concept - checking whether it contains duplicates or not

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False