class MinStack:

    def __init__(self):
        self.continer=[]
        self.minContiner = []
        

    def push(self, val: int) -> None:
        self.continer.append(val)
        val=min (val, self.minContiner[-1] if self.minContiner else val)
        self.minContiner.append(val)

    def pop(self) -> None:
        self.continer.pop()
        self.minContiner.pop()
        

    def top(self) -> int:
        return self.continer[-1]
    
        

    def getMin(self) -> int:
        return self.minContiner[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()