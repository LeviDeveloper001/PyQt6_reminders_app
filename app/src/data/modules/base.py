import typing as t
import sys
import json

PATH_TO_JSON_DATA_DIR = '\\'.join(sys.path[0].split('\\')[:-1]) + '\\data\\'


    
class Item:
    def __init__(self, _id,  item_data:dict):
        self.id=_id
        self.data = item_data
            
    def set_props(self):
        for n, v in self.data.items():
            self.__setattr__(n, v)
            
    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}) {self.data}'
            

class Manager:
    path_to_json=None
    item_class=Item
    
    def __init__(self):
        self.__init_data()
    
    def __init_data(self):
        with open(self.path_to_json, 'r', encoding='utf-8') as json_file:
            self.__data = json.loads(json_file.read())
    
    
    def __normilize_data(self, data:dict=None):
        data = data if isinstance(data, dict) else self.__data
        final_data = {}
        for k, v in data.items():
            final_data[str(k)] = v
        data = final_data
        return data
    
    @property
    def data(self):
        return self.__data.copy()
    
    def update_data(self, update_data:dict):
        self.__data = {**self.__data, **self.__normilize_data(update_data)}
        
    
    
    @data.setter
    def data(self, data:t.Dict[str, t.Any]):
        self.__data = self.__normilize_data(data)
        
    def save_data(self):
        with open(self.path_to_json, 'w', encoding='utf-8') as json_file:
            json_file.write(
                json.dumps(
                    self.__normilize_data(self.__data)
                )
            )
    
            
    def get_item(self, _id):
        return self.item_class(_id, self.data[str(_id)])
        
        



    

        
