class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        hashmap = {}
        for num in nums: hashmap[num] = hashmap.get(num, 0) + 1
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for num in hashmap:
                if hashmap[num] != 0: 
                    perm.append(num)
                    hashmap[num] = hashmap[num] - 1
                    dfs()
                    perm.pop()
                    hashmap[num] = hashmap[num] + 1
        dfs()
        return res