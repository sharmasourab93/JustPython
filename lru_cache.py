"""
Python: LRU Cache

There are several ways to implement LRU Cache:
    1. Using Ordered Dictionary
    2. Creating an Object Using Queue & Hash Map/Dict
"""


class LRUCache:
    
    def __init__(self, capacity: int):
        
        self.cache = list()
        self.cap = capacity
    
    def insert(self, data):
        
        if 0 <= len(self.cache) < self.cap:
            self.cache.insert(0, data)
            
        else:
            self.cache.pop()
            self.cache.insert(0, data)
            
    def __call__(self):
        
        print(self.cache)
            
        
if __name__ == '__main__':
    caches = LRUCache(3)
    print("Inserting 1")
    caches.insert(1)
    caches()
    print("Inserting 2, 3")
    caches.insert(2)
    caches.insert(3)
    caches()
    print("Inserting 4")
    caches.insert(4)
    caches()
    caches.insert(5)
    caches()
