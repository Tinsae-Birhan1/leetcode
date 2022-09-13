class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        
       
        for item in range(len(s)):
            if s[item]!="]":
                stack.append(s[item])
           
            else:
                container= "" 
                while stack[-1]!='[':
                    container=stack.pop() + container
                stack.pop()
                
                x=""
                while stack and stack[-1].isdigit():
                    x=stack.pop() + x
                stack.append(int(x)*container)
        return "".join(stack)