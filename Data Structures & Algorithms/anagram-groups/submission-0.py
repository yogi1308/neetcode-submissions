class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {} # sorted - nums index
        for i in range(len(strs)):
            sorted_string = "".join(sorted(strs[i]))
            if sorted_string in hash_map:
                hash_map[sorted_string].append(i)
            else:
                hash_map[sorted_string] = [i]
        print(hash_map)
        arr = []
        hash_arr_map = {} # sorted - arr index
        for string in hash_map:
            arr.append([])
            for idx in hash_map[string]:
                arr[len(arr) - 1].append(strs[idx])

        return arr



