class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_copy = set()
        for num in nums:
            if num in nums_copy:
                return True
            nums_copy.add(num)
        return False



#    def hasDuplicate(self, nums: List[int]) -> bool:
#        nums_copy = nums[0:]
#        for num in nums:
#            nums_copy.remove(num)
#            if num in nums_copy:
#                return True
#        return False
