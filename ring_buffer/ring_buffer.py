class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.current = 0
        self.storage = [None] * capacity

    # added function to be able to append data into ringbuffer
    def append(self, item):
        self.storage[self.current] = item

        if self.current < self.capacity - 1:
            self.current += 1
        else:
            self.current = 0

    # function to return data
    def get(self):
        items = []
        for i in self.storage:
            if i is not None:
                items.append(i)
        print(items)
        return items 