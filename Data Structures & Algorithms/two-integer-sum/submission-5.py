class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            val = nums[i]
            if val in my_dict:
                my_dict[val].append(i)
            else:
                my_dict[val] = [i]
        print(my_dict)
        for num in my_dict:
            comp = target - num
            if comp in my_dict:
                if my_dict[num] != my_dict[comp]:
                    return [my_dict[num][0], my_dict[comp][0]]
                elif my_dict[num] == my_dict[comp] and len(my_dict[num]) > 1:
                    return [my_dict[num][0], my_dict[num][1]]