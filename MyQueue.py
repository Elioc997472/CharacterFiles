class myStack:

    def __init__(self, maxsize=0):
        self._maxsize = maxsize
        self.vals []

    def push(self, value):
        if len(self.vals)<maxsize or maxsize==0:
            self.vals.append(value)
        else:
            raise RuntimeError("Cannot push item. Stack is already full!")

    def pop(self):
        return self.vals.pop()

    def peek(self):
        return self.vals[len(vals)-1]

    def isEmpty(self):
        return len(self.vals)==0
