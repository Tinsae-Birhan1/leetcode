class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if not len(stack):
                stack.append(c)
                continue
            
            if c == ')' and stack[-1] == '(':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(c)
        
        return not len(stack)
