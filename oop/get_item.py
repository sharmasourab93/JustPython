

class RandomClass:
    
    def __init__(self):
        self.obj = list()
    
    def __getitem__(self, item: int):
        return self.obj[item]
        
        
if __name__ == '__main__':
    test = RandomClass()
    test.obj = [1, 2, 3, 4, 5]
    print(test[:])
