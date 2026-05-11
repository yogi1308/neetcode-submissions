class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return

        mid = len(nums) // 2
        a1 = nums[:mid]
        a2 = nums[mid:]

        self.sortColors(a1)
        self.sortColors(a2)

        nums[:] = self.Merge(a1, a2)

    def Merge(self, a1, a2):
        a1_ptr = a2_ptr = 0
        new = []

        while a1_ptr < len(a1) and a2_ptr < len(a2):
            if a1[a1_ptr] < a2[a2_ptr]:
                new.append(a1[a1_ptr])
                a1_ptr += 1
            else:
                new.append(a2[a2_ptr])
                a2_ptr += 1

        if a1_ptr < len(a1):
            new.extend(a1[a1_ptr:])
        else:
            new.extend(a2[a2_ptr:])

        return new
