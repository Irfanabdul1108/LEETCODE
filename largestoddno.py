# platform - leetcode
#link - https://leetcode.com/problems/largest-odd-number-in-string/description/
# concept - largest odd number substring in a string

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                return num[:i+1]
        return ""

