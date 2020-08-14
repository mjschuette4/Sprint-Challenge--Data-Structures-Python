class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity
        self.length = 0

    def append(self, item):
        self.storage[self.current] = item
        #increment
        self.current += 1 
        #increment
        self.length += 1  
        #When current is at max, current % capacity = 0, sets current to 0 and the item is replaced
        self.current %= self.capacity 

    def get(self):
        print(self.storage[:self.length])
        return self.storage[:self.length]