# platform - leetcode
#link - https://leetcode.com/problems/count-primes/description/
# concept -  counting primes

class Solution {
public:
    int countPrimes(int n) {
             vector<int> primes(n, 0);
        int ans = 0;

        for(int i=2; i<n; i++)
        {
            if(primes[i] == 0)
            {
                ans++;
                
                for(int j=2*i; j<n; j+=i)
                {
                    if(primes[j] == 0)
                    {
                        primes[j] = 1;
                    }
                }
            }
        }

        return ans;         
    }
};