class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False
        new_nums = nums[:len(nums)]
        idx = -1
        base_idx = 0
        while not found and new_nums:
            mid = round(len(new_nums) / 2)
            print(new_nums, new_nums[mid])
            if new_nums[mid] == target:
                idx = base_idx + mid
                found = True
                print("exec", idx)
            elif new_nums[mid] < target:
                new_nums = new_nums[mid + 1:]
                base_idx += mid + 1
            else:
                new_nums = new_nums[:mid]
                base_idx += 0
        return idx

