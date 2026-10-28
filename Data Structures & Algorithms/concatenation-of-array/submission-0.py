class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        

        ume = list(nums)
        for i in nums:
            ume.append(i)
        return ume