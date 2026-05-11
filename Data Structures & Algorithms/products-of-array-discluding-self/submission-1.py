class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total_product = 1
        has_zero = 0
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                has_zero += 1

        if has_zero == 0:
            [output.append(int(total_product / num)) for num in nums]
        elif has_zero == 1:
            [output.append(total_product) if num == 0 else output.append(0) for num in nums]
        else :
            [output.append(0) for num in nums]
        return output
