class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1, ptr2 = 0, 1
        copies = False
        for i in range(len(nums)):
            if ptr2 >= len(nums): break
            print("val1", nums[ptr1], "ptr1", ptr1, "val2", nums[ptr2], "ptr2", ptr2)
            if nums[ptr1] != nums[ptr2]:
                ptr1 += 1
                ptr2 += 1
            else: 
                del nums[ptr2]
                copies = True
        return len(nums)