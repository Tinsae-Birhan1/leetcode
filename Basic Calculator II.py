class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        num=0
        operators='+'
        for item in range(len(s)):
            if s[item].isdigit():
                num=num*10+ int(s[item])
            if s[item] in ['+', '-', '*', '/'] or item==len(s)-1:
                
                if operators=='+':
                    stack.append(num)
                elif operators=='-':
                    stack.append(-num)
                elif operators=="*":
                    x=stack.pop()
                    y=x*num
                    stack.append(y)
                else:
                    x=stack.pop()
                    y=int(x/num)
                    stack.append(y)
                operators=s[item]
                num=0
                
                
                
        return sum(stack)
                
            