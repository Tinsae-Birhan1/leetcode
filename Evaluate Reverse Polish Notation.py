class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        continer=[]
       
        for y in tokens:     
            
            if y== "+":
                continer.append(continer.pop() + continer.pop())
                
            elif y== "-":
                a, b =continer.pop(), continer.pop()
                continer.append(b-a)
            elif y== "*":
                continer.append(continer.pop() * continer.pop())

            elif y== "/":
                a, b =continer.pop(), continer.pop()
                continer.append(int(b/a))
            else:
                continer.append(int(y))
               
        return continer[0]