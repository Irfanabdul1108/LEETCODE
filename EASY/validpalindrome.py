# platform - leetcode
#link - https://leetcode.com/problems/valid-palindrome/
# concept - checking whether it is a valid palindrome or not

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        n=len(s)
        j=n-1
        while(i<j):
            if(s[i]==''):
                i+=1
            if(s[j]==''):
                j-=1
            if(s[i].isalnum()==False):
                i+=1
            if(s[j].isalnum()==False):
                j-=1
            if(s[i]!=''and s[j]!=''and s[i].isalnum()==True and s[j].isalnum()==True):
                if (s[i].lower()==s[j].lower()):
                    i+=1
                    j-=1
                else:
                    return False
        return True
