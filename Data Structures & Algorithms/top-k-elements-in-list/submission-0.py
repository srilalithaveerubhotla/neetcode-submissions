class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dicte ={}
        nume =[]
        for i in nums:
            if i in dicte:
                dicte[i] +=1
            else:
                dicte[i] =1
        for i, v in dicte.items():
            if v>=k:
                nume.append(i)
        return nume

        