from typing import Dict, Any

class State:
    def __init__(self, name:str, data:Dict=None):
        self.__name = self.__class__.__name__ + '_' + name
        if isinstance(data, dict): self.__data=data
        elif data is None: self.__data={}
        else: raise TypeError(f'Аргумент "data" должен быть dict или None, а не {type(data)}')
        
    @property
    def name(self):
        return self.__name
    
    @property
    def data(self):
        return self.__data.copy()
    
    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.name==value.name
        elif isinstance(value, str):
            return self.name==value
        return False



class StateCollection:
    @property
    def state_dict(self):
        return self.__dict__
        
        


