# platform - leetcode
#link - https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
# concept -  Check If a Word Occurs As a Prefix of Any Word in a Sentence

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i, word in enumerate(words):
            if word.startswith(searchWord): return i+1
        return -1