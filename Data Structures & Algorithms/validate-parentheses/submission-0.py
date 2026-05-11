class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in close_open:
                if len(stack) > 0 and stack[-1] == close_open.get(char):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0