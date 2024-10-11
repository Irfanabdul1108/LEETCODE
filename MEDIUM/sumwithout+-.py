# platform - leetcode
#link - https://leetcode.com/problems/sum-of-two-integers/
# concept -  sum of two numbers without using  +,-  operators

class Solution:
    def getSum(self, a: int, b: int) -> int:
       l=[a,b]
       return sum(l)
        
        
# time complexity - O(1)

class Solution {
public:
    int getSum(int a, int b) {
        int temp=0;
        while(b!=0){
            temp=(a&b)<<1;
            a=(a^b);
            b=temp;
        }
        return a;
    }
};

