# platform - leetcode
#link -  https://leetcode.com/problems/reverse-integer/
# concept - reverse integer

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])
        
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        
        return res
    
    
    # most optimized 
    
    class Solution {
public:
    int reverse(int x) {
        int i=0,res=0,rem;
        int sign=(x<0)?-1:1;
        int m=abs(x);
        while(m)
        {
            rem=m%10;
                   if (res> INT_MAX/10 || (res == INT_MAX / 10 && rem > 7)) return 0;
            if (res < INT_MIN/10 || (res == INT_MIN / 10 && rem < -8)) return 0;
         res=res*10+rem;
         m=m/10;
       i++;
        }
        return res*sign;
    }
};
    