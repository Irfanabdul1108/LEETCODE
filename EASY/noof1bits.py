# platform - leetcode
#link - https://leetcode.com/problems/number-of-1-bits/
# concept - count no of 1 bits

#  timecomplexity --> O(logn)
class Solution:
    def hammingWeight(self, n: int) -> int:
        m=bin(n)[2:]
        return m.count('1')
    
    
#  timecomplexity --> O(1)


class Solution {
public:
    int hammingWeight(uint32_t n) {
     int count=0;
     while(n)
     {
      if(n&1==1)
  count++;
  n=n>>1;
     }
     return count;
    }
};
    
        