# platform - leetcode
#link - https://leetcode.com/problems/add-digits/description/
# concept - adding each and every digit from a number

 
class Solution:
    def addDigits(self, num: int) -> int:
        if(num==0):
            return 0
        elif(num%9==0):
            return 9
        else:
            return num%9