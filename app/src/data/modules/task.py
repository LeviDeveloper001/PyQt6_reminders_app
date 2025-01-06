import datetime as dt

from .base import Manager, Item, PATH_TO_JSON_DATA_DIR


class TaskItem(Item):
    pass    


class TasksManager(Manager):
    path_to_json=PATH_TO_JSON_DATA_DIR+'tasks.json'
    item_class = TaskItem
    
    

    


