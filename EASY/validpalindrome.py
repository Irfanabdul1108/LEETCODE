# platform - leetcode
#link - https://leetcode.com/problems/valid-palindrome/
# concept - somewhat diff from normal palindrome concept

class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1="abcdefghijklmnopqrstuvwxyz1234567890"
        m=""
        p=s.lower()
        for i in p:
            if i in str1:
                m+=i
        if m==m[::-1]:
            return True
        else:
            return False

        