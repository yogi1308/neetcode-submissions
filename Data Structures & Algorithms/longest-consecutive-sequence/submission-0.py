class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            val = num
            cons = 1
            while val + 1 in nums:
                cons += 1
                val += 1
            if cons > res:
                res = cons
        return res

        