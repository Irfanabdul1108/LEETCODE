# platform - leetcode
#link - https://leetcode.com/problems/rotate-string/
# concept -  rotate string 

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        list1=[]
        for i in range(len(s)):
            list1.append(s[i])
        for i in range(len(s)):
            list1.remove(s[i])
            list1.append(s[i])
            str1=''.join(map(str,list1))
            if str1==goal:
                return True
        return False

        
