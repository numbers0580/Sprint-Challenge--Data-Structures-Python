class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.position = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            # Not full yet, just append node to end
            self.storage.append(item)
        else:
            # Ring Buffer is full, find oldest node to replace

            # Insert new node at correct position in ring buffer
            self.storage.insert(self.position, item)
            
            # But now because of insert, the ring buffer is one node too many
            # Oldest data was pushed to position + 1. Remove it
            self.storage.pop(self.position + 1)

            # Iterate/Cycle the position counter
            self.position += 1
            if self.position >= self.capacity:
                self.position = 0

    def get(self):
        return [found for found in self.storage if found != None]