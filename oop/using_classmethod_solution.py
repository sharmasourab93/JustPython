"""
Python: Use @classmethod Polymorphism to Construct Objects Generically
"""
import os


# The problem boils down to needing a generic way to construct objects
# In other languages, you'd solve this problem
# with constructor polymorphism, requiring that each InputData
# Subclass provides a special constructor that can be used generically
# by the helper methods that orchestrate the MapReduce.
# The trouble is that Python only allows
# for the single constructor method __init__.
# The best way to solve this problem is with @classmethod polymorphism
# this is exactly like the instance method
# polymorphism used for InputData.read, except that it applies to whole
# classes instead of their constructed ob jects.
class GenericInputData:
    
    def read(self):
        raise NotImplementedError
    
    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError
    

class PathInputData(GenericInputData):
    
    def read(self):
        return open(self.path).read()
    
    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))
