# platform - leetcode
#link - https://leetcode.com/problems/palindrome-number/description/
# concept - check it is palindrome number or not 


class Solution:
    def isPalindrome(self, x: int) -> bool:
        m=str(x)
        if m==m[::-1]:
            return True
        else:
            return False