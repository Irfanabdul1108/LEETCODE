# platform - leetcode
#link  - https://leetcode.com/problems/plus-one/
# concept - check if both the strings are same or not (where one string is jumbeld and another string is not jumbeld)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = ''.join(map(str, digits))
        m=int(str1)+1
        return [
        int(p) 
        for p in str(m)
        ]
        
        
