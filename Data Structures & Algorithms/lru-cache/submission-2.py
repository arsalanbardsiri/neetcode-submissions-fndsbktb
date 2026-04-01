class LRUCache:

    def __init__(self, capacity: int):
      self.capacity = capacity
      self.maps = {}
      self.track_call = []

    def put(self, key: int, value: int) -> None:
    
      if key in self.maps:
            self.track_call.remove(key)
      
      self.maps[key] = value
      self.track_call.append(key)

      if len(self.maps) > self.capacity:
        lru = self.track_call.pop(0)  # Remove oldest key
        self.maps.pop(lru)


    def get(self, key: int) -> int:


      if key in self.maps:
        self.track_call.remove(key)
        self.track_call.append(key)
        return(self.maps[key])

      else:
        return(-1)
        