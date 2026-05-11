class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        done = {}
        return_set = []
        all_vals = set()
        for num in nums:
            if num not in all_vals:
                if nums.count(num) in done:
                    done[nums.count(num)].append(num)
                else:
                    done[nums.count(num)] = [num]
                all_vals.add(num)

        sorted_done = sorted(done)[::-1]
        print(done)
        for num in sorted_done:
            if len(return_set) != k:
                for val in done[num]:
                    if len(return_set) != k:
                        return_set.append(val)
                    else:
                        return return_set
            else:
                return return_set
        return return_set



