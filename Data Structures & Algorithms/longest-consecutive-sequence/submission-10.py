class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        nums_set = sorted(nums_set)

        max_streak = 1
        curr_streak = 1
        prev_num = None
        for num in nums_set:
            if num - 1 == prev_num:
                curr_streak += 1
                if curr_streak > max_streak:
                    max_streak = curr_streak
            else:
                curr_streak = 1
            prev_num = num
        return max_streak
        
        

        