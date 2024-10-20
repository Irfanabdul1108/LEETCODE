//platform - leetcode
//link - https://leetcode.com/problems/find-the-peaks/description/
//concept - find the peaks


#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> findPeaks(vector<int>& mountain) {
         int size=mountain.size();
        vector<int>v;
      int count=0;
     for(int i=1;i<size-1;i++)
      {
          if(!(mountain[i-1]<mountain[i] && mountain[i+1]<mountain[i])){
                  count++;
                        }
          if(count==0)
          {
              v.push_back(i);
              }
         count=0;
      }
        return v;
};
