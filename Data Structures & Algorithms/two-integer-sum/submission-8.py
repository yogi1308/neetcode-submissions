class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in my_dict:
                val = nums[i]
                return [my_dict[comp], i]
            my_dict[nums[i]] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            curr_val = nums[i]
            for j in range(i + 1, len(nums)):
                if curr_val + nums[j] == target:
                    return [i, j]

