class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #width = right -left
        #capacity = min(right, width) * width 
        left =0
        maxcap =0
        right = len(heights)-1

        while left <  right:
            width = right -left
            capacity = min(heights[left], heights[right])*width 
            maxcap = max(maxcap,capacity)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return maxcap       



        