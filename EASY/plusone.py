# platform - leetcode
#link  - https://leetcode.com/problems/plus-one/
# concept - add one at last of the list

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = ''.join(map(str, digits))
        m=int(str1)+1
        return [
        int(p) 
        for p in str(m)
        ]
        
        
