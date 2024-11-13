# platform - leetcode
#link - https://leetcode.com/problems/first-unique-character-in-a-string/
# concept - length of the last word in a given string


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        m=s.split()
        return len(m[-1])
        
