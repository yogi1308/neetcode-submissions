class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        for i in range(len(nums)):
            num = nums[i]
            cons = 1
            while num + 1 in nums_set:
                cons += 1
                num += 1
            if cons > res:
                res = cons
        return res

        