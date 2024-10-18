# platform - leetcode
#link - https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/description/
# concept - find all lonely numbers in the array where i+1 and i-1 also should not be there

from collections import Counter
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        list1=[]
        dict1=Counter(nums)
        for i,j in dict1.items():
            if j==1 and i+1 not in dict1 and i-1 not in dict1:
                list1.append(i)
        return list1
