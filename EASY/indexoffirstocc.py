# platform - leetcode
#link - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# concept - finding the index of the first occurrence of the string(heystack variable) in a string(needle variable)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        