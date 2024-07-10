# platform - leetcode
#link - https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-n-to-1-without-loop
# concept - check whether palindrome or not

class Solution:
    def isPalindrome(self, x: int) -> bool:
        m=str(x)
        if m==m[::-1]:
            return True
        else:
            return False

