class Solution:
    def sortColors(self, nums: List[int]) -> None:
        dicte = {}

        for i in nums:
            dicte[i] = dicte.get(i, 0) + 1

        result = []
        for key in sorted(dicte.keys()):
            result += [key] * dicte[key]

        nums[:] = result