class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # if we reserve sertain amount of memory for the list in very beginning, it makes our 
        # program more officiant then add more clasters into list later
        self.values = [None] * capacity
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
        # result = []
        # for i in self.values:
        #     if i:
        #         result.append(i)
        # return result
        return [x for x in self.values if x is not None]