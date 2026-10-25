class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dicte = defaultdict(list)
        for i in strs:
            sroted = ''.join(sorted(i))
            dicte[sroted].append(i)
        return list(dicte.values())
            
        