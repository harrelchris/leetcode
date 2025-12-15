class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for i in s:
            if i in parens:
                if stack == []:
                    return False
                if stack.pop() != parens[i]:
                    return False
            else:
                stack.append(i)
        else:
            return stack == []
