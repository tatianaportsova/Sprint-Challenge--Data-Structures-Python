# class RingBuffer:
#     def __init__(self, capacity):
#         self.ringBuffer = []
#         self.capacity = capacity

#     def append(self, item):
#         if len(self.ringBuffer) < self.capacity:
#             self.ringBuffer.append(item)
#         else:
#             self.ringBuffer.pop(0)
#             self.ringBuffer.append(item)

#     def get(self):
#         return self.ringBuffer

class RingBuffer:
    def __init__(self, capacity):
        self.ringBuffer = []
        self.capacity = capacity
        self.added = 0

    def append(self, item):
        if self.added <= (self.capacity - 1):
            self.ringBuffer.insert(self.added, item)
            self.added += 1
        else:
            index = self.added % self.capacity
            self.added += 1
            self.ringBuffer[index] = item

    def get(self):
        return self.ringBuffer
