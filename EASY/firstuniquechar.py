# platform - leetcode
#link - https://leetcode.com/problems/first-unique-character-in-a-string/
# concept -  first unique character in string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict={}
        for char in s:
            if char not in dict:
                dict[char]=True
            else:
                dict[char]=False
        for i,c in enumerate(s):
            if dict[c]==True:
                return i
        return -1

