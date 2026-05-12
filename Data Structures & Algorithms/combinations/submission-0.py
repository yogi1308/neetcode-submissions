class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n + 1)]
        res = []
        def dfs(idx, subset):
            if len(subset) == k:
                res.append(subset.copy())
                return
            for i in range(idx, len(arr)):
                subset.append(arr[i])
                dfs(i + 1, subset)
                subset.pop()
        dfs(0, [])
        return res
        

# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         candidates.sort()
#         def dfs(idx, subset):
#             if sum(subset) >= target:
#                 if sum(subset) == target:
#                     res.append(subset.copy())
#                 return
#             for i in range(idx, len(candidates)):
#                 if i > idx and candidates[i] == candidates[i - 1]:
#                     continue
#                 subset.append(candidates[i])
#                 dfs(i + 1, subset)
#                 subset.pop()
#         dfs(0, [])
#         return res