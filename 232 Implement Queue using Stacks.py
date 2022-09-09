class Queue:
    def __init__(self):
        self.in_stk = []
        self.out_stk = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stk.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())

        self.out_stk.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())

        return self.out_stk[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.out_stk and not self.in_stk
