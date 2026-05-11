class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result_array = []
        for l in range(len(nums) - k + 1):
            result_array.append(max(nums[l : l + k]))
        return result_array