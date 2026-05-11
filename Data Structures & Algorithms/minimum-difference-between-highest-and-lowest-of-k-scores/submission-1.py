class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l, r = 0, k
        nums = sorted(nums)
        print(nums)
        min_diff = max(nums)
        while r < len(nums)  + 1:
            arr = nums[l : r]
            highest, lowest = max(arr), min(arr)
            if min_diff > (highest - lowest): min_diff = (highest - lowest)
            print(arr, min_diff)
            l, r = l + 1, r + 1
        return min_diff
                