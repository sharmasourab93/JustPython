"""
Python: Use Multiple Inheritance Only for Mix-in Utility Class
"""
import json


class ToDictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)
    
    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        
        return output
    
    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


# Mix-ins can also be composed together.
# Fox example, say you want a mix-in that provides
# generic JSON serilization for any class.
# You can do this by assuming that a class provides a to_dict method
class JsonMixin:
    
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)
    
    def to_json(self):
        return json.dumps(self.to_dict())


# Note how the JsonMixin class defines both
# instance methods and class methods.
# Mixins let you add either kind of behaviour.

class DatacenterRack(ToDictMixin, JsonMixin):
    def __init__(self, switch=None, machines=None):
        self.switch = Switch(**switch)
        self.machines = [
            Machine(**kwargs) for kwargs in machines
            ]
        

class Switch(ToDictMixin, JsonMixin):
    pass


class Machine(ToDictMixin, JsonMixin):
    pass


if __name__ == '__main__':
    serialized = """{
        "switch": {"ports": 5, "speed": 1e9},
        "machine": [
            {"cores": 8, "ram": 32e9, "disk": 5e12},
            {"cores": 4, "ram": 16e9, "disk": 1e12},
            {"cores": 2, "ram": 4e9, "disk": 500e9}]
        }"""
    deserialized = DatacenterRack.from_json(serialized)
    roundtrip = deserialized.to_json()
    assert json.loads(serialized) == json.loads(roundtrip)
    
# Things to remember
# Avoid using multiple inheritance if mix-in classes
# can achieve the same outcome
# Use pluggable behaviours at the instance level to provide
# per-class customization when mix-in classes may  require it.
# Compose mix-ins to create complex functionality from simple behaviors
