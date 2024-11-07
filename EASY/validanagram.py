# platform - leetcode
#link - https://leetcode.com/problems/valid-anagram/description/
# concept - find the valid anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for i in s:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]= dict1.get(i,0)+1
        for i in t:
                if i in dict2:
                    dict2[i]+=1
                else:
                    dict2[i]= dict2.get(i,0)+1
        if dict1==dict2:
            return  True
        return False
