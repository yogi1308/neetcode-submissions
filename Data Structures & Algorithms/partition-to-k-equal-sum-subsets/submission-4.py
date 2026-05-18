
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        subsetTotal = sum(nums) // k
        used = [False] * len(nums)
        if subsetTotal != total / k:
            return False

        nums.sort(reverse=True)
        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == subsetTotal:
                return backtrack(0, k - 1, 0)
            
            for j in range(i, len(nums)):
                if not used[j] and subsetSum + nums[j] <= subsetTotal:
                    used[j] = True
                    if backtrack(j + 1, k, subsetSum + nums[j]): return True
                    used[j] = False
            return False
        
        return backtrack(0, k, 0)