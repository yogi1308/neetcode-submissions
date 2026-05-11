class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            max = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    max = j - i
                    break
            result.append(max)
        return result