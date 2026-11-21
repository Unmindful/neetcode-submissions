class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open_parenthesis = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in close_to_open_parenthesis:
                if stack and stack[-1] == close_to_open_parenthesis[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        