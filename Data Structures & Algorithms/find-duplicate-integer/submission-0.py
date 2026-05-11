class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > 1: return num