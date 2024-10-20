# platform - leetcode
#link -  https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/description/
# concept - count the no of words which starts and ends with vowels 
    
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        list2=['a','e','i','o','u']
        count=0
        for i,j in enumerate(words):
            if (i>=left and i<=right) and j[0] in list2 and j[len(j)-1] in list2:
                count+=1
        return count
