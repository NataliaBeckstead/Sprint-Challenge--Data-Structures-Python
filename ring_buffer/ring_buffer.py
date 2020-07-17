class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = []
        self.index = 0

    def append(self, item):
        if len(self.values) < self.capacity:
            self.values.append(item)
        else:
            self.values[self.index] = item
            if self.index < len(self.values) - 1:
                self.index += 1
            else:
                self.index = 0

    def get(self):
        # return self.values
        result = []
        for i in self.values:
            if i:
                result.append(i)
        return result