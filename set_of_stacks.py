"""
A class that implements a set of stacks, where each stack has a maximum capacity.

The `SetOfStacks` class allows you to push and pop items onto and from a set of stacks. 
When a stack reaches its maximum capacity, a new stack is created and subsequent items are added to the new stack. 
When a stack becomes empty, it is removed from the set of stacks.

Attributes:
    capacity (int): The maximum capacity of each stack.
    stacks (list): A list of stacks, where each stack is a list of items.

Methods:
    push(item): Adds an item to the set of stacks.
    pop(): Removes and returns the last item from the set of stacks.
    __str__(): Returns a string representation of the set of stacks.
"""
class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [[]] 

    def push(self, item):
        if len(self.stacks[-1]) == self.capacity:  # if the last stack is at capacity
            self.stacks.append([])  # create a new stack
        self.stacks[-1].append(item)  # add the new item to the last stack

    def pop(self):
        if len(self.stacks[-1]) == 0:  # if the last stack is empty
            if len(self.stacks) == 1:  # if there's only one stack
                return None
            else:
                self.stacks.pop()  # remove the last stack
        return self.stacks[-1].pop()  # remove and return the last item from the last stack

    def __str__(self):
        return str(self.stacks)


if __name__=='__main__':
    stacks = SetOfStacks(3)

    print("Pushing items onto stacks:")
    for i in range(10):
        stacks.push(i)
        print(stacks)

    print("\nPopping items from stacks:")
    for i in range(10):
        print("Popped:", stacks.pop())
        print(stacks)
