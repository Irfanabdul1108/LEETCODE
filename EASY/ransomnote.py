# platform - leetcode
#link - https://leetcode.com/problems/ransom-note/
# concept - Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#           Each letter in magazine can only be used once in ransomNote.

from collections import Counter
class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        if len(m)<len(r):
            return False
        dict1=dict(Counter(m))
        dict2=dict(Counter(r))
        for i,j in dict2.items():
            if j>dict1.get(i,0):
                return False 
        return True

        