class LRUCache:

    def __init__(self, capacity: int):
      self.capacity = capacity
      self.cache = OrderedDict()

    def get(self, key: int) -> int:
        #if doesn't exist return -1
        if key not in self.cache:
            return -1
        
        #if it is move it, to most recent call then return it
        self.cache.move_to_end(key)
        return self.cache[key]


    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)