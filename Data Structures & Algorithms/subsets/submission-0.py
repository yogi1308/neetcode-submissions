class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # global parameters
        subset = []
        idx = 0

        solution = []

        def visitAll():
            # without `nonlocal` we'd just be setting local variables
            nonlocal idx, subset, solution

            # base case
            if idx == len(nums):
                # `subset` is global and will change if we don't copy it
                solution.append(subset.copy())
                return

            # recursion
            
            idx += 1 # add 1
            visitAll()
            idx -= 1 # undo

            subset.append(nums[idx]) # add nums[idx]
            idx += 1 # add 1
            visitAll()
            idx -= 1 # undo 
            subset.pop() # undo

        visitAll()
        return solution