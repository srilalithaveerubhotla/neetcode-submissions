class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dicte = {}
        for i,j in enumerate(nums):
            if target -j in dicte:
                return [dicte[target-j],i]
            dicte[j] =i
        return list()
       
            
        