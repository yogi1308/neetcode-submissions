class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights) + 1):
                heights_arr = heights[i : j]
                if heights_arr == []: min_height = 0
                else: min_height = min(heights_arr)
                width = len(heights_arr)
                area = min_height * width
                print(heights_arr, min_height, width, area)
                if area > max_area:
                    max_area = area
        return max_area
