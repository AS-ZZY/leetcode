class LRUCache(dict):
    def __init__(self, capacity: int):
        self.c = capacity

    def get(self, key: int) -> int:
        if key in self:
            self[key] = self.pop(key)
            return self[key]    
        return -1    

    def put(self, key: int, value: int) -> None:
        key in self and self.pop(key) 
        self[key] = value
        len(self) > self.c and self.pop(next(iter(self)))
