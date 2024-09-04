# platform - leetcode
#link - https://leetcode.com/problems/valid-perfect-square/description/
# concept - valid perfect square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = num**0.5
        if n==int(n):
            return True
        else:
            return False

        
