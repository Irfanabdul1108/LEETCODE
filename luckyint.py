# platform - leetcode
#link - https://leetcode.com/problems/find-lucky-integer-in-an-array/description/
# concept -  finding the number which is lucky according to given condition in the question 

from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        list2=[-1]
        dict1=dict(Counter(arr))
        for i,j in dict1.items():
            if i==j:
                list2.append(i)
        return max(list2)

        