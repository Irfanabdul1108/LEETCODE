# platform - leetcode
#link - https://leetcode.com/problems/sqrtx/description/
# concept - find the square root of x without any built in functions


class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        while(left<=right):
            mid=(left+right)//2
            if(mid*mid==x):
                return mid
            if((mid*mid)<x):
                left=mid+1
            if((mid*mid)>x):
                right=mid-1
        return right