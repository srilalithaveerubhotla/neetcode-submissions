class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best =0
        kin = set(nums)
        print(kin)
        for i in nums:
            if (i - 1) not in kin:
                length =1
                while (i + length) in kin:
                    length +=1
                best = max(best,length)
        return best


        