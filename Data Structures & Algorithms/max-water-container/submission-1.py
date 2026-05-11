class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = (len(heights)-1)*(min(heights[0], heights[len(heights)-1]))
        for l in range(0, len(heights) - 2):
            for r in range(len(heights) -1, l, -1):
                width = r - l
                min_height = min(heights[r], heights[l])
                area = width*min_height
                if area > max_vol:
                    max_vol = area
        return max_vol