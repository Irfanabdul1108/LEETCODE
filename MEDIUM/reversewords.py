# platform - leetcode
#link -https://leetcode.com/problems/reverse-words-in-a-string/description/
# concept - reverse words in a string
class Solution:
    def reverseWords(self, s: str) -> str:
        m=s.split()
        k=m[::-1]
        res=' '.join(map(str,k))
        return res