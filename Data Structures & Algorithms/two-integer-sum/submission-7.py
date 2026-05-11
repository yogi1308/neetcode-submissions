class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            print("comp", comp, "val", nums[i], my_dict)
            if comp in my_dict:
                val = nums[i]
                return [my_dict[comp], i]
            else:
                my_dict[nums[i]] = i