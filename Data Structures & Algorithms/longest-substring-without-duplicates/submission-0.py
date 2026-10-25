class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dicte = {}
        maxie =""
        left = 0

        for right in range(len(s)):
            if s[right] in dicte and dicte[s[right]] >= left:
                left = dicte[s[right]]+1
            dicte[s[right]] = right 
        
            current = s[left:right+1]
            if len(current)>len(maxie):
                maxie = current



        