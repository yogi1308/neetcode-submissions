class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        trapped = []
        for curr_pos in range(1, len(height)):
            max_left = 0
            for idx in range(curr_pos - 1, -1, -1):
                max_left = max(max_left, height[idx])

            max_right = 0
            for idx in range(curr_pos + 1, len(height), 1):
                max_right = max(max_right, height[idx])

            if height[curr_pos] < min(max_left, max_right):
                total_water += min(max_left, max_right) - height[curr_pos]
                trapped.append(min(max_left, max_right) - height[curr_pos])
        print(trapped)
        return total_water


