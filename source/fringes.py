import heapq
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)

    def delete_elements(self, num_elements):
        for i in range(num_elements):
            self.dequeue()


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)

    def delete_elements(self, num_elements):
        for i in range(num_elements):
            self.dequeue()

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def size(self):
        return len(self.elements)

    def clear_priority_queue(self):
        while not self.is_empty():
            self.get()
