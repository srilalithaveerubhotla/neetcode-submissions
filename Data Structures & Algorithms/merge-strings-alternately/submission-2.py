class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        left =0
        string =""

        while left <len(word1) or left < len(word2):
            if left <len(word1):
                string +=word1[left]
            if left < len(word2):
                string +=word2[left]
            left +=1
        return string
