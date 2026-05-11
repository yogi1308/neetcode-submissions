class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if ((nums[i] + nums[j]) * (-1)) in nums:
                    third_num = None
                    for k in range(len(nums)):
                        if k == i or k == j:
                            continue
                        if ((nums[i] + nums[j]) * (-1)) is nums[k]:
                            third_num = nums[k]
                            arr = [nums[i], nums[j], third_num]
                            arr = sorted(arr)
                            if arr not in res:
                                res.append(arr)
                                
        return res
