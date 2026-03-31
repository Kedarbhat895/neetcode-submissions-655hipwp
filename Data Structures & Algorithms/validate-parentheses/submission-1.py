class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        opened = {"(", "{", "["}
        mapping = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in opened:
                stack.append(i)
            else:
                if stack and stack[-1] != mapping[i]:
                    return False
                if not stack:
                    return False
                stack.pop()
    
        if len(stack) > 0:
            return False
        return True

        