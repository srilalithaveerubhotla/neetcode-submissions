class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        final = []
        for i in matrix:
            for j in i:
                final.append(j)
        print(final)
        left =0
        right = len(final)-1
        while left <= right:
            mid = (left+right)//2
            if final[mid]==target:
                return True
            elif final[mid]<target:
                left = mid +1
            else:
                right = mid -1
        return False
