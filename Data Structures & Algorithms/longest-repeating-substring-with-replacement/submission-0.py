class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dicte ={}
        left =0
        res =0
        maxf =0
        for right in range(len(s)):
            if s[right] in dicte:
                dicte[s[right]] +=1
            else:
                dicte[s[right]] =1
            maxf = max(maxf,dicte[s[right]])
            while (right-left+1) -maxf >k:
                dicte[s[left]] -=1
                left +=1
            res = max(res, right-left+1)
        return res
            
        