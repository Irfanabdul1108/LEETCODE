# platform - leetcode
#link - https://leetcode.com/problems/power-of-two/description/
# concept -  power of two 
    

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        elif (n&(n-1)):
            return False
        else:
            return True 
        