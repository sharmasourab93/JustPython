"""
Python: Use @classmethod Polymorphism to Construct Objects Generically
Reference: Effective Python by Brett Slatkin
"""
import os
from threading import Thread


# Polymorphism is a way for multiple classes in a hierarchy to
# implement their own unique versions of a method.
# This allows many classes to fulfill the same interface or
# abstract base class while providing different functionality.
class InputData:
    
    def read(self):
        raise NotImplementedError
    

class PathInputData(InputData):
    
    def __init__(self, path):
        super().__init__()
        self.path = path
        
    def read(self):
        return open(self.path).read()


# An abstract interface for the MapReduce worker that consumes
# the input data in a standard way.
class Worker:
    
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None
        
    def map(self):
        raise NotImplementedError
    
    def reduce(self, other):
        raise  NotImplementedError
    

# A Concrete Subclass worker to implement
# the specific MapReduce function
# for applying : a simple newline counter.
class LineCountWorker(Worker):
    
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')
        
    def reduce(self, other):
        self.result += other.result
        
        
def generate_inputs(data_dir):
    
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))
        

def create_workers(input_list):
    workers = []
    
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
        
    return workers


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    
    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()
        
    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
        
    return first.result


# Finally Connecting all the pieces together
def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


# The Problem:
# The huge issue is the mapreduce function is not generic at all.
# If you want to write another InputData or Worker subclass,
# You would also have to rewrite the generate_inputs,
# create_workers, and mapreduce functions to match.

