class stack():
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        self.items.pop()

    def isempty(self):
        return self.items == []

    def peek(self):
        if not self.isempty():
            return self.items[-1]

    def display_array(self):
        print(self.items)


s = stack()
s.push(1)
s.push(2)
s.push(3)
# s.pop()
s.display_array()
print(s.peek())