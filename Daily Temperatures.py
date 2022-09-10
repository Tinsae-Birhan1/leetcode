class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [0]* len(temperatures)
        stack=[]
        
        
        for i, x in enumerate(temperatures):
            while stack and x > stack[-1][0]:
                stackX, stackInd= stack.pop()
                solution[stackInd]= (i-stackInd)
            stack.append([x, i])
        return solution